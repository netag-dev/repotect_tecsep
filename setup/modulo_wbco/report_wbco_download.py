from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
import sys,os,locale
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit, QWidget
import modulo_wbco.wbcoController
    


# Classe Para Geração dos Reports
class GerarReport:
    def gerar_pdf(self,filename,report_cabecalho,well_information,wbco_primary,wbco_back_up,employe):

        def caminho_absoluto_desktop():
            idioma_sistema = locale.getdefaultlocale()[0].lower()

            if "pt" in idioma_sistema:
                return os.path.join(os.path.expanduser("~"), "Desktop")
            else:
                return os.path.join(os.path.expanduser("~"), "Desktop")

        caminho_desktop = caminho_absoluto_desktop()

        c = canvas.Canvas(caminho_desktop+"/"+filename, pagesize=A4,bottomup=False)  # alternatively use bottomup=False
        width, height = A4

        value_info = report_cabecalho
        value_well_information = well_information

        value_wbco_primary = wbco_primary
        value_wbco_back_up = wbco_back_up

        value_employe = employe

        
        
        data = [
                        ["Shift (Day/NIgth):", value_info[4], "Approved By:",value_info[13]],
                        ["Job Type:", value_info[3], "Prepared By:",value_info[8]],
                        ["Filed/Location:", value_info[2], "Well NUmber:",value_info[7]],
                        ["Rig Name:", value_info[1], "Customer Name:",value_info[6]],
                        ["Job Ref. Number:", value_info[0], "Report Date:",value_info[5]],
        ]

        data_well_information =   [
                    [value_well_information[0], value_well_information[1], value_well_information[2],value_well_information[3],value_well_information[4],value_well_information[5],value_well_information[6],value_well_information[7]],
                    ["Casing Size", "Length", "OD","ID","Size"," Weight", "Volume Capacity","Hole Volume"]
                    
                ]

        data_wbco_primary =  value_wbco_primary +[
                   
                    
                    ["Description", "Size", "Thread Coonections","OD","ID"," Drift Size"]
                ]


        data_wbco_back_up = value_wbco_back_up + [
                    ["Description", "Size", "Thread Coonections","OD","ID"," Drift Size"]
                ]

        data_on_going = [
                    [value_info[9]],
                    
                ]

        data_wbco_activity = [
                    [value_info[10]],
                    
                ]

        data_wbco_enginner = [
            [value_employe[0],value_employe[1],value_employe[2],""],
            [value_info[8],value_info[11],value_info[12],""],
            ["WBCO Tools Enginer (Days)","Shift","Total Days",""]
        ]


        #TBaela Well Infomration
        new_table = Table(data_well_information, colWidths=[34*mm,24*mm,17*mm,17*mm,22*mm,18*mm,34*mm,34*mm])

        #Tabela REport Information
        table = Table(data, colWidths= [40*mm,72*mm,38*mm,49.7*mm])
        #table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        #                ("ALIGN", (0,0), (-1,-1), "LEFT"),
        #                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)])

        table_wbco_primary = Table(data_wbco_primary,colWidths=[75*mm,18*mm,50*mm,19*mm,19*mm,19*mm])

        table_wbco_backup = Table(data_wbco_back_up,colWidths=[75*mm,18*mm,50*mm,19*mm,19*mm,19*mm])

        table_on_going_activity = Table(data_on_going,colWidths=200*mm)

        table_wbco_activity = Table(data_wbco_activity,colWidths=200*mm)

        table_wbco_enginer = Table(data_wbco_enginner,colWidths=[90*mm,30*mm,40*mm])

        padding = 3
        table.setStyle([
                    
                    #('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                    ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                    ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                    ('VALIGN',(0,0),(0,-1),'MIDDLE'),
                    ("LINEABOVE", (0,0), (-1,0), 2, colors.black),
                    ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                    ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                    #('BACKGROUND', (0, 1), (-1, -1), colors.white)
                    #('GRID',(0,0),(-1,-1),1,colors.black)
                    ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,3,alpha=85)),
                    ("BACKGROUND", (3,5),(1,-6),colors.PCMYKColor(0,1,1,3,alpha=85)),
                    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)
                ])

        new_table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 2, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        table_wbco_primary.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 2, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ("ALIGN", (0,0), (-1,-1), "CENTER"),
                        ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,3,alpha=85)),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])


        table_wbco_backup.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 2, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "CENTER"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,3,alpha=85)),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        table_on_going_activity.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 2, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        table_wbco_activity.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])


        table_wbco_enginer.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 2, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        

        table.wrapOn(c, width, height)
        table.drawOn(c, 5*mm, 33*mm)

        

        new_table.wrapOn(c, width,height)
        new_table.drawOn(c,5*mm,83*mm)

        table_wbco_primary.wrapOn(c,width,height)
        table_wbco_primary.drawOn(c,5*mm,108*mm)

        altura_wbco_primary = table_wbco_primary._height
        print(altura_wbco_primary)

        table_wbco_backup.wrapOn(c,width,height)
        table_wbco_backup.drawOn(c,5*mm,( (108*mm) + (altura_wbco_primary) + 35))

        altura_wbco_back_up = table_wbco_backup._height
        print(altura_wbco_back_up)

        table_on_going_activity.wrapOn(c,width,height)
        table_on_going_activity.drawOn(c,5*mm,((108*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33)

        altura_on_going_activity = table_on_going_activity._height
        print(altura_on_going_activity)

        table_wbco_activity.wrapOn(c,width,height)
        table_wbco_activity.drawOn(c,5*mm,((108*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33 + altura_on_going_activity + 30)

        table_wbco_enginer.wrapOn(c,width,height)
        table_wbco_enginer.drawOn(c,5*mm,210*mm)

        styles = getSampleStyleSheet()    


        width = 2.5 * inch  # largura da imagem
        height = 1 * inch  # altura da imagem




        #Borda Para a Pagina
        c.setFillColorRGB(1,0,0)
        c.rect(12,12,571,800)

        styles = {
            'Normal': ParagraphStyle(
                'normal',
                fontSize=10,
                textColor='black',
                spaceAfter=12,
            ),
            'Estilo_texto_titulo': ParagraphStyle(
                'estilo_texto_titulo',
                fontSize=11,
                textColor='#0018F9',
                spaceAfter=5,
                underline = True
            ),
            'Estilo_texto_url': ParagraphStyle(
                'estilo_texto_url',
                fontSize=12,
                textColor='#0018F9',
                spaceAfter=12,
            ),

            'Estilo_titulo_tabela': ParagraphStyle(
                'estilo_titulo_tabela',
                fontSize=10,
                textColor='#0018F9',
                spaceAfter=12,
            ),
        }

        img = ImageReader("img/img.png",styles["Estilo_texto_titulo"])
        c.drawImage(img, 5*mm, 5*mm, width, height, mask='auto')


        width = 7.8 * inch  # largura da imagem
        height = 2 * inch  # altura da imagem

        #img_certificate = ImageReader("img/arrendoda.png",styles["Estilo_texto_titulo"])
        #c.drawImage(img_certificate,5*mm,230*mm,width,height,mask='auto')

        

        
        ptext = "Daily Report #"+str(value_well_information[8])+" WBCO Tools Service "
        ptlink = " www.tecsep-tsg.com"
        pwell_information = " Well Information"
        p_wbco_tools_primary = " WBCO Tools On board (primary)"
        p_wbco_tools_back_up = "WBCO Tools On board (Back Up)"
        p_ong_going_activity = "Ongoing Rig Activity"
        p_text_lema = '"Proudly Tecsep, Proudly African"'



        p = Paragraph(ptext, style=styles["Estilo_texto_titulo"])
        plink = Paragraph(ptlink, style=styles["Estilo_texto_url"])
        pwell = Paragraph(pwell_information, style= styles["Estilo_titulo_tabela"])
        p_wbco_primary = Paragraph(p_wbco_tools_primary, style= styles["Estilo_titulo_tabela"])
        p_wbco_back_up = Paragraph(p_wbco_tools_back_up, style= styles["Estilo_titulo_tabela"])
        p_ong_going = Paragraph(p_ong_going_activity,style=styles["Estilo_titulo_tabela"])
        p_wbco_activity = Paragraph("WBCO Tools Activity",style=styles["Estilo_titulo_tabela"])

        p_lema = Paragraph(p_text_lema,style = styles["Normal"])


        p.wrapOn(c, 70*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 130*mm, 15*mm)    # position of text / where to draw

        plink.wrapOn(c,70*mm,60*mm)
        plink.drawOn(c,145*mm,22*mm)

        pwell.wrapOn(c,50*mm,50*mm)
        pwell.drawOn(c,5*mm,80*mm)

        p_wbco_primary.wrapOn(c,70*mm,50*mm)
        p_wbco_primary.drawOn(c,5*mm,106*mm)

        p_wbco_back_up.wrapOn(c,70*mm,50*mm)
        p_wbco_back_up.drawOn(c,5*mm,(108*mm) + (altura_wbco_primary) + 25)

        p_ong_going.wrapOn(c,70*mm,50*mm)
        p_ong_going.drawOn(c,5*mm,((108*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 25 )

        p_wbco_activity.wrapOn(c,70*mm,50*mm)
        p_wbco_activity.drawOn(c,5*mm,((108*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33 + altura_on_going_activity + 25)

        p_lema.wrapOn(c,70*mm,60*mm)
        p_lema.drawOn(c,7*mm,283*mm)


        c.save()
