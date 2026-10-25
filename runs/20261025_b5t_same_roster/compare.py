import csv, json, math
S='<scratch b5t_vs>'; D='/home/lilhelper/Downloads'
b5t={r['isotope'].replace('-',''):dict(split=r['split'],err=float(r['observed'])-float(r['B5T_3D_TENSOR_PRINCIPAL_prediction']),err_b4=float(r['observed'])-float(r['B4_COORD_BASELINE_prediction'])) for r in csv.DictReader(open(f'{S}/B5T_PREDICTIONS.csv'))}
t240={r['isotope']:r for r in json.load(open(f'{D}/isotope_residuals_240_tensor_20261017/data.json'))['rows']}
s253={r['isotope']:r for r in json.load(open(f'{D}/isotope_residuals_253_20261017/data.json'))['rows']}
rmse=lambda xs: math.sqrt(sum(x*x for x in xs)/len(xs))
for name,rows in (('BULK_INTENSIVE_TENSOR',t240),('BULK_NORMALIZED_SPIN',s253)):
    common=[i for i in rows if i in b5t]
    for b5split in ('development','held'):
        for p in sorted(set(rows[i]['partition'] for i in common)):
            sel=[i for i in common if rows[i]['partition']==p and (b5t[i]['split']=='development')==(b5split=='development')]
            if sel: print(name,b5split,p,len(sel),rmse([b5t[i]['err'] for i in sel]),rmse([b5t[i]['err_b4'] for i in sel]),rmse([rows[i]['evaluation_residual'] for i in sel]))
