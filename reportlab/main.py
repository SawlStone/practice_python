# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Image

import csv

data_file = 'data.csv'


def import_data(data_file):
    attendee_data = csv.reader(open(data_file, 'rb'))
    for row in attendee_data:
        first_name = row[0]
        last_name = row[1]
        employment = row[2]
        pdf_file_name = first_name + last_name + '_' + employment + '.pdf'
        generate_sertificate(first_name, last_name, employment, pdf_file_name)


def generate_sertificate(first_name, last_name, employment, pdf_file_name):
    attendee_name = first_name + ' ' + last_name
    c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))

    # header text
    c.setFont('Helvetica', 48, leading=None)
    c.drawCentredString(415, 500, 'Employee Certificate')
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 450, 'This certificate is presented to:')
    # attendee name
    c.setFont('Helvetica-Bold', 34, leading=None)
    c.drawCentredString(415, 395, attendee_name)
    # for completing the...
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 350, 'who holds the position in the IT company of:')
    # employment
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415, 310, employment)
    # image of seal
    seal = 'certificate.ico'
    c.drawImage(seal, 350, 150, width=100, height=100)

    c.showPage()

    c.save()

import_data(data_file)
