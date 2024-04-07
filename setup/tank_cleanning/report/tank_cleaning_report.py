from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
import sys,locale,os
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit, QWidget
import tank_cleanning.pack_report.reportController
import tank_cleanning.pack_shift.shiftController
import tank_cleanning.pack_daily_progress.dayshift_activityController
import tank_cleanning.pack_hse.hseController
    


# Classe Para Geração dos Reports
class GerarReport:
    def gerar_pdf(self,filename,report_cabecalho,lista_turno_diurno,lista_turno_noturno,lista_actividade,lista_man_produtive_hour,lista_tank_information,lista_hse,listar_non_produtive_man,lista_consumiveis,lista_ppe):



        def caminho_absoluto_desktop():
            idioma_sistema = locale.getdefaultlocale()[0].lower()

            if "pt" in idioma_sistema:
                return os.path.join(os.path.expanduser("~"), "Desktop")
            else:
                return os.path.join(os.path.expanduser("~"), "Desktop")

        caminho_desktop = caminho_absoluto_desktop()

        c = canvas.Canvas(caminho_desktop+"/"+filename, pagesize=A4,bottomup=False)
        width, height = A4

        dados_cabebacalho = report_cabecalho
        dados_turno_diurno = lista_turno_diurno
        dados_turno_noturno = lista_turno_noturno
        dados_actividades = lista_actividade
        dados_man_produtive = lista_man_produtive_hour
        dados_tank_information = lista_tank_information
        dados_hse = lista_hse
        dados_non_produtive = listar_non_produtive_man
        dados_consumiveis = lista_consumiveis
        dados_ppe = lista_ppe

        
        
        data = [
                        ["Shift (Day/NIgth):", dados_cabebacalho[5], "Approved By:",dados_cabebacalho[9]],
                        ["Job Type:", dados_cabebacalho[4], "Prepared By:",dados_cabebacalho[8]],
                        ["Filed/Location:", dados_cabebacalho[3], "",],
                        ["Rig Name:", dados_cabebacalho[2], "Customer Name:",dados_cabebacalho[7]],
                        ["Job Ref. Number:", dados_cabebacalho[1], "Report Date:",dados_cabebacalho[6]]
        ]

        data_dayshift =  dados_turno_diurno + [

            
           
            ["Name","Personnel Position","Planned Demob","Crew "]
        ]

        data_nigthshift = dados_turno_noturno + [
            
            ["Name","Personnel Position","Planned Demob","Crew "]
            

        ]

        data_project_description = [
             
             ["Project Description",dados_actividades[0]]
             
             ]


        data_hse_title = [["HSE (update daily)"]]

        data_hse = dados_hse + [ 
            
            #["Safety Observations","0","NO sAFETY oBSERVATION Camied out today"],
            #["Near Miss Cards","0","NO sAFETY oBSERVATION Camied out today"],
            #["Permit Audit","0","NO sAFETY oBSERVATION Camied out today"],
            #["Site Audits","0","NO sAFETY oBSERVATION Camied out today"],
            #["Safety Meetings","0","NO sAFETY oBSERVATION Camied out today"],
            ["","Qty","Comments"]
            ]
        
        data_title_dayshift = [
            ["Dayshift"]
        ]

        data_daily_progress_tittle = [["Daily Progress"]]

        data_daily_progress = [
            [dados_actividades[1]]
        ]

        label_planed_activities = [
            ["Planned Activities (Next 24hrs)"]
        ]

        data_planned_activities = [
            [dados_actividades[2]]
        ]

        label_norm_reading = [
            ["NORM Reading result and contamination control"]
        ]
        data_norm_reading = [
            [dados_actividades[3] ]
        ]
        label_equipament = [
            ["Equipament and Materials"]
        ]
        data_equipament = [
            [dados_actividades[4]]
        ]

       

        data_tank_information = dados_tank_information + [
            
            ["Tank Number","Type West","Volume West","Tank Type"]
        ]

        label_man_produtive_hour = [
            ["Productive Man Hour Report"]
        ]

        data_man_produtive_hour = dados_man_produtive + [
            ["Work Order Number","Description"," Original Hours \n  Estimated","Hours Worked \n     Today","  O/T Worked \n      Today","Hours Worked \n    To Date","      Hours \n Remaining","    Visual % \n Complete"]
        ]


        label_non_produtive_man_hour = [
            ["Non Productive Man Hour Report"]
        ]

        data_non_produtive_man_hour = dados_non_produtive + [

            ["","Hours Today","Comments"]
        ]

        label_inventory_mob = [
            ["Inventory mob"]
        ]


        data_competency_profile = dados_consumiveis + dados_ppe +  [
            ["Name","Quantity Used","Consumables"]
        ]


        





        total_linha_dayshift = data_dayshift.__len__()

        total_linha_nightshift = data_nigthshift.__len__()

        total_linha_tank_information = data_tank_information.__len__()

        tatal_hour_personel = data_man_produtive_hour.__len__()

        total_imbo_inventory = data_competency_profile.__len__()

        print(total_imbo_inventory)

        
       

        style = getSampleStyleSheet()["Normal"]
        style.alignment = 1 
        

        
        table = Table(data, colWidths= [40*mm,72*mm,38*mm,49.7*mm])

        table_dyshift = Table(data_dayshift,colWidths= [30*mm,25*mm,24*mm,10*mm])

        tabe_nightshit = Table(data_nigthshift,colWidths=[30*mm,25*mm,24*mm,10*mm])

        table_descriptio_project = Table(data_project_description,colWidths = [40*mm,160*mm])

        table_hse_title = Table(data_hse_title,colWidths=[200*mm])

        table_hse = Table(data_hse,colWidths=[40*mm,30*mm,130*mm])

        tabe_title_dayshift = Table(data_title_dayshift,colWidths=[200*mm])

        table_daily_progress_title = Table(data_daily_progress_tittle,colWidths=[200*mm])

        table_daily_progress = Table(data_daily_progress,colWidths=[200*mm])

        table_planed_activities_title = Table(label_planed_activities,colWidths=[200*mm])

        table_planed_activities = Table(data_planned_activities,colWidths=[200*mm])

        table_norm_reading_title = Table(label_norm_reading,colWidths=[200*mm])

        table_norm_reading = Table(data_norm_reading,colWidths=[200*mm]) 

        table_equipament_title = Table(label_equipament,colWidths=[200*mm])

        table_equipament = Table(data_equipament,colWidths=[200*mm]) 

        table_tank_information = Table(data_tank_information,colWidths=[50*mm]) 


        table_man_produtive_hour_title = Table(label_man_produtive_hour,colWidths=[200*mm]) 

        table_man_produtive_hour = Table(data_man_produtive_hour,colWidths=[27*mm,53*mm,20*mm]) 

 
        table_non_produtive_man_hour_title = Table(label_non_produtive_man_hour,colWidths=[200*mm])   

        tablenon_produtive_man_hour = Table(data_non_produtive_man_hour,colWidths=[40*mm,30*mm,130*mm])  

        table_competency_profile_title = Table(label_inventory_mob,colWidths=[200*mm]) 

        table_man_competency_profile = Table(data_competency_profile,colWidths=[66.7*mm]) 

        padding = 2
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
                    ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,3,alpha=85)),
                    ("BACKGROUND", (3,5),(1,-6),colors.PCMYKColor(0,1,1,3,alpha=85)),
                    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)
                ])
        

        table_dyshift.setStyle([
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ('TEXTCOLOR',(0,4),(3,4), colors.black),
                        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('BACKGROUND',(0,total_linha_dayshift - 1),(3,total_linha_dayshift -1 ),colors.PCMYKColor(0,1,1,3)),
                        ("ALIGN", (0,0), (-1,-1), "LEFT")])
        

        tabe_nightshit.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ('TEXTCOLOR',(0,4),(3,4), colors.black),
                        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('BACKGROUND',(0,total_linha_nightshift - 1),(3,total_linha_nightshift -1 ),colors.PCMYKColor(0,1,1,3)),
                        ("ALIGN", (0,0), (-1,-1), "LEFT")])
        
        
        table_descriptio_project.setStyle([("ALIGN",(0,0),(1,0), "LEFT"),
                                           ("FONTSIZE",(0,0),(-1,-1),8),
                                           ("GRID",(0,0),(-1,-1),0.25, colors.black),
                                           ("BOX",(0,0),(-1,-1),0.25, colors.black),
                                           
                                           ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                           ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                           ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                           ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                           ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3))])
        

        
        table_hse.setStyle([("ALIGN",(0,0),(1,0), "LEFT"),
                                           ("FONTSIZE",(0,0),(-1,-1),8),
                                           ("GRID",(1,0),(-1,-1),0.25, colors.black),
                                           ("BOX",(0,0),(-1,-1),0.25, colors.black),
                                           ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                           ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                           ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                           ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                           ('ALIGN',(1,0),(1,5),"CENTER"), # Centralizar a coluna quantidade
                                           ('ALIGN',(2,5),(2,5), "CENTER"),
                                           ("BACKGROUND",(0,0),(0,5),colors.PCMYKColor(0,1,1,3))])
        
        table_hse_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        tabe_title_dayshift.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding)])
        
        table_daily_progress_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        table_daily_progress.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        

        table_planed_activities_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        table_planed_activities.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        table_norm_reading_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        table_norm_reading.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BOX",(0,0),(0,0),0.25,colors.black)]) 
        
        table_equipament_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        table_equipament.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BOX",(0,0),(0,0),0.25,colors.black)]) 
        

        table_tank_information.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(-1,-1),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                ("BACKGROUND",(0,3),(3,4),colors.PCMYKColor(0,1,1,3)),
                                ('ALIGN',(0,0),(3,total_linha_tank_information),"CENTER"),
                                ("BOX",(0,0),(-1,-1),0.25,colors.black)])
        
        table_man_produtive_hour_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        
        table_man_produtive_hour.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(-1,-1),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                ('ALIGN',(0,0),(7,tatal_hour_personel),"CENTER"),
                                ('ALIGN',(0,2),(1,2),"CENTER"),
                                ("BOX",(0,0),(-1,-1),0.25,colors.black)])
        

        table_non_produtive_man_hour_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        

        tablenon_produtive_man_hour.setStyle([("ALIGN",(0,0),(1,0), "LEFT"),
                                           ("FONTSIZE",(0,0),(-1,-1),8),
                                           ("GRID",(1,0),(-1,-1),0.25, colors.black),
                                           ("BOX",(0,0),(-1,-1),0.25, colors.black),
                                           ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                           ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                           ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                           ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                           ('ALIGN',(1,0),(1,8),"CENTER"), # Centralizar a coluna quantidade
                                           ('ALIGN',(2,5),(2,5), "CENTER"),
                                           ("BACKGROUND",(0,0),(0,8),colors.PCMYKColor(0,1,1,3))])
        

        table_competency_profile_title.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(0,0),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ("BACKGROUND",(0,0),(0,0),colors.PCMYKColor(0,1,1,3)),
                                ("BOX",(0,0),(0,0),0.25,colors.black)])
        

        table_man_competency_profile.setStyle([("ALIGN",(0,0),(0,0),"LEFT"),
                                ("FONTSIZE",(0,0),(-1,-1),8),
                                ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Espaçamento inferior das células
                                ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                                ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                ('ALIGN',(0,0),(2,total_imbo_inventory),"CENTER"),
                                ("BOX",(0,0),(-1,-1),0.25,colors.black)])
        

        

        table.wrapOn(c, width, height)
        table.drawOn(c, 5*mm, 33*mm)

        table_dyshift.wrapOn(c,width,height)
        table_dyshift.drawOn(c,5*mm,65*mm)

        tabe_nightshit.wrapOn(c,width,height)
        tabe_nightshit.drawOn(c,110*mm,65*mm)

        altura_day = table_dyshift._height
        altura_nigth = tabe_nightshit._height
        altura_table_dayshift = 0

        if altura_day >= altura_nigth:
            altura_table_dayshift = altura_day
        else:
            altura_table_dayshift = altura_nigth


        table_descriptio_project.wrapOn(c,width,height)
        table_descriptio_project.drawOn(c,5*mm,( (65*mm) + (altura_table_dayshift) + 10 ))

        altura_description = table_descriptio_project._height

        table_hse_title.wrapOn(c,width,height)
        table_hse_title.drawOn(c,5*mm,((65*mm) + (altura_table_dayshift) + 5 + (altura_description) + 9 ))

        table_hse.wrapOn(c,width,height)
        table_hse.drawOn(c,5*mm,((65*mm) + (altura_table_dayshift) + 5 + (altura_description) + 23))


        altura_table_hse = table_hse._height

        tabe_title_dayshift.wrapOn(c,width,height)
        tabe_title_dayshift.drawOn(c,5*mm,((65*mm) + (altura_table_dayshift) + 13 + (altura_description) + 23) + (altura_table_hse) + 1 )

        altura_table_tittle_dayshift = tabe_title_dayshift._height

        table_daily_progress_title.wrapOn(c,width,height)
        table_daily_progress_title.drawOn(c,5*mm,(((65*mm) + (altura_table_dayshift) + 10 + (altura_description) + 23) + (altura_table_hse) + 1) + (altura_table_tittle_dayshift) + 2)

        altura_table_daily_progress_title = table_daily_progress_title._height + (((65*mm) + (altura_table_dayshift) + 10 + (altura_description) + 23) + (altura_table_hse) + 1) + (altura_table_tittle_dayshift) + 2

        table_daily_progress.wrapOn(c,width,height)
        table_daily_progress.drawOn(c,5*mm,altura_table_daily_progress_title )

        altura_table_daily_progress = table_daily_progress._height + altura_table_daily_progress_title

        table_planed_activities_title.wrapOn(c,width,height)
        table_planed_activities_title.drawOn(c,5*mm,altura_table_daily_progress)

        altura_table_planed_activities_title = table_planed_activities_title._height + altura_table_daily_progress

        table_planed_activities.wrapOn(c,width,height)
        table_planed_activities.drawOn(c,5*mm,altura_table_planed_activities_title)

        altura_table_planed_activities = table_planed_activities._height + altura_table_planed_activities_title

        table_norm_reading_title.wrapOn(c,width,height)
        table_norm_reading_title.drawOn(c,5*mm,altura_table_planed_activities)

        altura_table_norm_reading_title = table_norm_reading_title._height + altura_table_planed_activities

        table_norm_reading.wrapOn(c,width,height)
        table_norm_reading.drawOn(c,5*mm,altura_table_norm_reading_title)

        altura_table_norm_reading = table_norm_reading._height + altura_table_norm_reading_title

        table_equipament_title.wrapOn(c,width,height)
        table_equipament_title.drawOn(c,5*mm,altura_table_norm_reading)
        
        altura_table_equipament_title = table_equipament_title._height + altura_table_norm_reading


        table_equipament.wrapOn(c,width,height)
        table_equipament.drawOn(c,5*mm,altura_table_equipament_title)

        altura_table_equipament = table_equipament._height + altura_table_equipament_title

        table_tank_information.wrapOn(c,width,height)
        table_tank_information.drawOn(c,5*mm,altura_table_equipament + 10)

        altura_table_tank_information = table_tank_information._height + altura_table_equipament 


        table_man_produtive_hour_title.wrapOn(c,width,height)
        table_man_produtive_hour_title.drawOn(c,5*mm,altura_table_tank_information + 20)

        altura_table_man_produtive_hour_title = table_man_produtive_hour_title._height + altura_table_tank_information + 20

        table_man_produtive_hour.wrapOn(c,width,height)
        table_man_produtive_hour.drawOn(c,5*mm,altura_table_man_produtive_hour_title)

        altura_table_man_produtive_hour = table_man_produtive_hour._height + altura_table_man_produtive_hour_title + 10

        table_non_produtive_man_hour_title.wrapOn(c,width,height)
        table_non_produtive_man_hour_title.drawOn(c,5*mm,altura_table_man_produtive_hour)


        altura_table_non_produtive_man_hour_title = table_non_produtive_man_hour_title._height + altura_table_man_produtive_hour

        tablenon_produtive_man_hour.wrapOn(c,width,height)
        tablenon_produtive_man_hour.drawOn(c,5*mm,altura_table_non_produtive_man_hour_title)

        altura_tablenon_produtive_man_hour = tablenon_produtive_man_hour._height + altura_table_non_produtive_man_hour_title + 5


        table_competency_profile_title.wrapOn(c,width,height)
        table_competency_profile_title.drawOn(c,5*mm,altura_tablenon_produtive_man_hour)

        altura_table_competency_profile_title = table_competency_profile_title._height + altura_tablenon_produtive_man_hour


        table_man_competency_profile.wrapOn(c,width,height)
        table_man_competency_profile.drawOn(c,5*mm,altura_table_competency_profile_title)


        
           


        width = 2.5 * inch  # largura da imagem
        height = 1 * inch  # altura da imagem




        #Borda Para a Pagina
        c.setFillColorRGB(1,0,0)
        c.rect(12,12,571,800)

        styles = {
            'Normal': ParagraphStyle(
                'normal',
                fontSize=11,
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
                fontSize=11,
                textColor='#0018F9',
                spaceAfter=12,
            ),
        }

        img = ImageReader("img/img.png",styles["Estilo_texto_titulo"])
        c.drawImage(img, 5*mm, 5*mm, width, height, mask='auto')

        
        ptext = "Daily Report #"+str(dados_cabebacalho[0])+" Tank Cleaning "
        ptlink = " www.tecsep-tsg.com"
       
        p_wbco_tools_primary = " WBCO Tools On board (primary)"
        p_wbco_tools_back_up = "WBCO Tools On board (Back Up)"
        p_ong_going_activity = "Ongoing Rig Activity"



        p = Paragraph(ptext, style=styles["Estilo_texto_titulo"])
        plink = Paragraph(ptlink, style=styles["Estilo_texto_url"])
        
        


        p.wrapOn(c, 70*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 130*mm, 15*mm)    # position of text / where to draw

        plink.wrapOn(c,70*mm,60*mm)
        plink.drawOn(c,145*mm,22*mm)

        
    


        c.save()


