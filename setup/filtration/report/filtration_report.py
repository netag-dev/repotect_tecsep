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
import tempfile,psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit, QWidget
    


# Classe Para Geração dos Reports
class GerarReport:
    def gerar_pdf(self,filename,report_cabecalho,cabecalho_prepared,cabecalho_aproved,fluid_information,primeiro_ciclo,seg_ciclo,terc_ciclo,quart_ciclo,quint_ciclo,sext_ciclo,set_ciclo,oit_ciclo,fluid_analysis,ongoing,consumiveis,enginheiro):

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
        value_prepared = cabecalho_prepared
        value_aproved = cabecalho_aproved
        value_fluid_information = fluid_information
        value_fluid_sumary = primeiro_ciclo
        value_segundo_ciclo = seg_ciclo
        value_terceiro_ciclo = terc_ciclo
        value_quarto_ciclo = quart_ciclo
        value_quinto_ciclo = quint_ciclo
        value_sexto_ciclo = sext_ciclo
        value_setimo_ciclo = set_ciclo
        value_oitavo_cilco = oit_ciclo
        valur_sumary = fluid_analysis
        value_ongoing = ongoing
        value_consumiveis = consumiveis
        enginheiro = enginheiro


        lista = [2,3,5,6]

        
        for valor in lista:
            if value_fluid_sumary[valor] == "":
                value_fluid_sumary[valor] = 0

            if value_segundo_ciclo[valor] == "":
                value_segundo_ciclo[valor] = 0

            if value_terceiro_ciclo[valor] == "":
                value_terceiro_ciclo[valor] = 0

            if value_quarto_ciclo[valor] == "":
                value_quarto_ciclo[valor] = 0

            if value_quinto_ciclo[valor] == "":
                value_quinto_ciclo[valor] = 0

            if value_sexto_ciclo[valor] == "":
                value_sexto_ciclo[valor] = 0

            if value_setimo_ciclo[valor] == "":
                value_setimo_ciclo[valor] = 0

            if value_oitavo_cilco[valor] == "":
                value_oitavo_cilco[valor] = 0

        total_minute_per_cicles = int(value_fluid_sumary[2]) + int(value_segundo_ciclo[2]) + int(value_terceiro_ciclo[2]) + int(value_quarto_ciclo[2]) + int(value_quinto_ciclo[2]) + int(value_sexto_ciclo[2]) + int(value_setimo_ciclo[2]) + int(value_oitavo_cilco[2])
        
        total_volume_per_cicles = int(value_fluid_sumary[3]) + int(value_segundo_ciclo[3]) + int(value_terceiro_ciclo[3]) + int(value_quarto_ciclo[3]) + int(value_quinto_ciclo[3]) + int(value_sexto_ciclo[3]) + int(value_setimo_ciclo[3]) + int(value_oitavo_cilco[2])

        de_per_cicle_total = int(value_fluid_sumary[5]) + int(value_segundo_ciclo[5]) + int(value_terceiro_ciclo[5]) + int(value_quarto_ciclo[5]) + int(value_quinto_ciclo[5]) + int(value_sexto_ciclo[5]) + int(value_setimo_ciclo[5]) + int(value_oitavo_cilco[5])

        cartidge_filter_total = int(value_fluid_sumary[6]) + int(value_segundo_ciclo[6]) + int(value_terceiro_ciclo[6]) + int(value_quarto_ciclo[6]) + int(value_quinto_ciclo[6]) + int(value_sexto_ciclo[6]) + int(value_setimo_ciclo[6]) + int(value_oitavo_cilco[6])

        nome_prepared = ""
        nome_aproved = ""
        
        for nome in value_prepared:
            nome_prepared += str(nome)+"/"

        for nome in value_aproved:
            nome_aproved += str(nome)+"/"

        nome_prepared = nome_prepared.rstrip("/")
        nome_aproved = nome_aproved.rstrip("/")

        

        
        #value_well_information = well_information
        #
        #value_wbco_primary = wbco_primary
        #value_wbco_back_up = wbco_back_up
        #
        #value_employe = employe

        
        
        data = [
                        ["Shift (Day/NIgth):", value_info[5], "Approved By:",nome_aproved],
                        ["Job Type:", value_info[4], "Prepared By:",nome_prepared],
                        ["Filed/Location:", value_info[3], "Well NUmber:",value_info[8]],
                        ["Rig Name:", value_info[2], "Customer Name:",value_info[7]],
                        ["Job Ref. Number:", value_info[1], "Report Date:",value_info[6]],
        ]

        data_fluid_information =   value_fluid_information + [
                    ["Fluid Information", "Daily Total", "Desnity ","Viscosity","Hole Volume"," Vol Filtered to date"]
                    
                ]

        data_filtration_sumary =  [
                   
                    
                    ["Cartidge Filters",value_fluid_sumary[6],value_segundo_ciclo[6],value_terceiro_ciclo[6],value_quarto_ciclo[6],value_quinto_ciclo[6],value_sexto_ciclo[6],value_setimo_ciclo[6],value_oitavo_cilco[6],cartidge_filter_total],
                    ["D.E per cycle 20kg sx",value_fluid_sumary[5],value_segundo_ciclo[5],value_terceiro_ciclo[5],value_quarto_ciclo[5],value_quinto_ciclo[5],value_sexto_ciclo[5],value_setimo_ciclo[5],value_oitavo_cilco[5],de_per_cicle_total],
                    ["Volume per cycle "+value_fluid_sumary[4],value_fluid_sumary[3],value_segundo_ciclo[3],value_terceiro_ciclo[3],value_quarto_ciclo[3],value_quinto_ciclo[3],value_sexto_ciclo[3],value_setimo_ciclo[3],value_oitavo_cilco[3],total_volume_per_cicles],
                    ["Total minutes per cycle",value_fluid_sumary[2],value_segundo_ciclo[2],value_terceiro_ciclo[2],value_quarto_ciclo[2],value_quinto_ciclo[2],value_sexto_ciclo[2],value_setimo_ciclo[2],value_oitavo_cilco[2],total_minute_per_cicles],
                    ["Stop Time",value_fluid_sumary[1],value_segundo_ciclo[1],value_terceiro_ciclo[1],value_quarto_ciclo[1],value_quinto_ciclo[1],value_sexto_ciclo[1],value_setimo_ciclo[1],value_oitavo_cilco[1],""],
                    ["Start Time",value_fluid_sumary[0],value_segundo_ciclo[0],value_terceiro_ciclo[0],value_quarto_ciclo[0],value_quinto_ciclo[0],value_sexto_ciclo[0],value_setimo_ciclo[0],value_oitavo_cilco[0],""],
                    ["Cycles", "1", "2","3","4"," 5","6","7","8","Total"],
                ]


        data_fluid_analysis = valur_sumary+[
                    ["Wellbore Displacement", "", "Time","Pumping Time","Volume Pumped"," NTUs","TSS % Solids"]
                ]

        data_on_going = [
                    [value_ongoing[0]],
                    
                ]

        data_wbco_activity = [
                    [value_ongoing[1]],
                    
                ]
        
        data_consumibles = value_consumiveis + [
            ["Material For Filtration","Type","Opening Stock","Additional Stock","Total Stock","Daily Used","Total Used","Closing Bal"]
        ]

        data_wbco_enginner = enginheiro + [
            
            ["WBCO Tools Enginer (Days)","Shift","Total Days",""]
        ]


        #TBaela Well Infomration
        table_fluid_information = Table(data_fluid_information, colWidths=[33.3*mm,33.3*mm,33.3*mm,33.3*mm,33.3*mm,33.3*mm])

        #Tabela REport Information
        table = Table(data, colWidths= [40*mm,72*mm,38*mm,49.7*mm])
        #table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        #                ("ALIGN", (0,0), (-1,-1), "LEFT"),
        #                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)])

        table_filtration_sumary = Table(data_filtration_sumary,colWidths=[35*mm,18.3*mm])

        table_fluid_analysis = Table(data_fluid_analysis,colWidths=[40*mm,25*mm,30*mm,35*mm,35*mm,15*mm,20*mm])

        table_on_going_activity = Table(data_on_going,colWidths=200*mm)

        table_wbco_activity = Table(data_wbco_activity,colWidths=200*mm)

        table_wbco_enginer = Table(data_wbco_enginner,colWidths=[90*mm,30*mm,40*mm])

        table_consumables = Table(data_consumibles, colWidths=[45*mm,20*mm,26*mm,23*mm,23*mm,23*mm,20*mm])

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

        table_fluid_information.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
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

        table_filtration_sumary.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
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


        table_fluid_analysis.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
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
        

        table_consumables.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
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

        

        table_fluid_information.wrapOn(c, width,height)
        table_fluid_information.drawOn(c,5*mm,70*mm)

        table_filtration_sumary.wrapOn(c,width,height)
        table_filtration_sumary.drawOn(c,5*mm,88*mm)

        altura_wbco_primary = table_filtration_sumary._height

        table_fluid_analysis.wrapOn(c,width,height)
        table_fluid_analysis.drawOn(c,5*mm,( (88*mm) + (altura_wbco_primary) + 35))

        altura_wbco_back_up = table_fluid_analysis._height

        table_on_going_activity.wrapOn(c,width,height)
        table_on_going_activity.drawOn(c,5*mm,((88*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33)

        altura_on_going_activity = table_on_going_activity._height

        table_wbco_activity.wrapOn(c,width,height)
        table_wbco_activity.drawOn(c,5*mm,((88*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33 + altura_on_going_activity + 30)

        altura_table_activity = table_wbco_activity._height + ((88*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33 + altura_on_going_activity + 60

        table_consumables.wrapOn(c,width,height)
        table_consumables.drawOn(c,5*mm,altura_table_activity)

        altura_table_consumiveis = table_consumables._height + altura_table_activity + 20

        table_wbco_enginer.wrapOn(c,width,height)
        table_wbco_enginer.drawOn(c,5*mm,altura_table_consumiveis)

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


        


        
        ptext = "Daily Report "+str(value_info[0])+"# Filtration "
        ptlink = " www.tecsep-tsg.com"
        pwell_information = " Fluid Information"
        p_wbco_tools_primary = " Filtration Summary"
        p_wbco_tools_back_up = "Fluid Analysis"
        p_ong_going_activity = "Ongoing Rig Activity"
        p_text_lema = '"Do it right the first time"'



        p = Paragraph(ptext, style=styles["Estilo_texto_titulo"])
        plink = Paragraph(ptlink, style=styles["Estilo_texto_url"])
        pwell = Paragraph(pwell_information, style= styles["Estilo_titulo_tabela"])
        p_wbco_primary = Paragraph(p_wbco_tools_primary, style= styles["Estilo_titulo_tabela"])
        p_wbco_back_up = Paragraph(p_wbco_tools_back_up, style= styles["Estilo_titulo_tabela"])
        p_ong_going = Paragraph(p_ong_going_activity,style=styles["Estilo_titulo_tabela"])
        p_wbco_activity = Paragraph("Filtration Activity",style=styles["Estilo_titulo_tabela"])
        p_lema = Paragraph(p_text_lema,style = styles["Normal"])


        width = 1.1 * inch  # largura da imagem
        height = 0.8 * inch  # altura da imagem

        image_data = value_info[9]

        # Salvar os dados da imagem em um arquivo temporário
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp_file.write(image_data)
        temp_file.close()

        print(temp_file.name)

        logo_cliente = ImageReader(temp_file.name,styles["Estilo_texto_titulo"])
        c.drawImage(logo_cliente,160*mm,8*mm,width,height,mask='auto')

        os.unlink(temp_file.name)


        p.wrapOn(c, 70*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 85*mm, 15*mm)    # position of text / where to draw

        plink.wrapOn(c,70*mm,60*mm)
        plink.drawOn(c,86*mm,22*mm)

        pwell.wrapOn(c,50*mm,50*mm)
        pwell.drawOn(c,5*mm,68*mm)

        p_wbco_primary.wrapOn(c,70*mm,50*mm)
        p_wbco_primary.drawOn(c,5*mm,85*mm)

        p_wbco_back_up.wrapOn(c,70*mm,50*mm)
        p_wbco_back_up.drawOn(c,5*mm,(88*mm) + (altura_wbco_primary) + 25)

        p_ong_going.wrapOn(c,70*mm,50*mm)
        p_ong_going.drawOn(c,5*mm,((88*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 25 )

        p_wbco_activity.wrapOn(c,70*mm,50*mm)
        p_wbco_activity.drawOn(c,5*mm,((88*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33 + altura_on_going_activity + 25)

        p_lema.wrapOn(c,70*mm,60*mm)
        p_lema.drawOn(c,80*mm,283*mm)


        c.save()

