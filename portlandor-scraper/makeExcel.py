import xlsxwriter
import csv
import time


filename = 'excel-{}.xlsx'.format(time.strftime('%Y%m%d-%H%M'))

workbook = xlsxwriter.Workbook(filename)

worksheet = workbook.add_worksheet()

info_section = workbook.add_format({
    'bold': True, 
    'bg_color': '#D3D3D3',
    'font_color': '#ffffff',
    'font_size': '16'
    })

worksheet.write('A1', 'Title', info_section)
worksheet.write('A2', 'Shortname', info_section)
worksheet.write('A3', 'Official Title', info_section)
worksheet.write('A4', 'Legacy Path', info_section)
worksheet.write('A5', 'News path for import', info_section)
worksheet.write('A6', 'Event path for import', info_section)
worksheet.write('A7', 'Parent', info_section)

worksheet.write('A8', 'Status')
worksheet.write('B8', 'Name/Title')
worksheet.write('C8', 'Type')
worksheet.write('D8', 'Subtype')
worksheet.write('E8', 'Legacy Path(s)')
worksheet.write('F8', 'Note')

with open('internal-20190620-2223.csv') as csvfile:
    linkreader = csv.reader(csvfile, delimiter= ',')
    for x in linkreader:
        y = 9
        count = 0
        worksheet.write('E{}'.format(y), count)
        y += 1
        count += 1
        print('Number of links loaded {}'.format(count))

workbook.close()

