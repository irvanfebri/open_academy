# from odoo import models

# class SessionXlsx(models.AbstractModel):
#     _name = 'report.febriacademy.report_session_xlsx'
#     _inherit = 'report.report_xlxs.abstract'

#     def generate_xlsx_report(self, workbook, data, session):
#         report_name = session.name

#         sheet = workbook.add_worksheet(report_name[:31])

#         headers = ["No","Name","Phone"]
#         bold = workbook.add_format({'bold': True})

#         for col_num, header in enumerate(headers): 
#             sheet.write(0, col_num, header, bold)
               

#         row_num = 1
#         for attendee in session.partner_ids:
#             sheet.write(row_num,0, '{}'.format(row_num or ''))
#             sheet.write(row_num,1, attendee.name or '')
#             sheet.write(row_num,2, attendee.phone or '')
#             row_num +=1


