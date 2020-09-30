from fpdf import FPDF
from datetime import datetime
import gen

g = gen.gen_excercise(3)
excercises = []
for i in range(25):
    excercises.append(next(g))

document = FPDF('P', 'mm', 'A4')
document.add_page()
document.set_font('Courier', size=15)

exiter = iter(excercises)
for _ in range(5):
    for x in range(5):
        text = gen.format_excercise(next(exiter))
        document.multi_cell(w=36, h=5, txt=text,
                            border=0, align='R')
    document.ln(40)

document.set_font('Helvetica', size=7)
exiter = iter(excercises)
for _ in range(5):
    for x in range(5):
        text = gen.get_result(next(exiter))
        document.cell(w=36, h=5, txt=text,
                      border=0, align='R')
    document.ln()

now = 'Soroban practice sheet generated at: '
now += datetime.now().strftime("%d/%m/%Y %H:%M:%S")
document.set_font('Helvetica', size=10)
document.set_y(-40)
document.cell(w=190, h=5, txt=now, border=0, align='C', ln=1)
document.cell(w=190, h=5, txt='(c)2020 by adamkov', border=0, align='C')
document.output("output.pdf")
