from PyPDF2 import PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4


from ..models import Dealer


def generate_report_name(dealer=None) -> str:
    # TODO generate report name using datetime
    return 'test_name'


def make_dealers_report():
    title = generate_report_name()
    canvas = Canvas(title, pagesize=A4)
    canvas.setTitle(title)

    canvas.save()


def make_dealer_report(dealer: Dealer):
    pass
