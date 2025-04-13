from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import csv
from statistics import mean

def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['Name'], float(row['Sales'])) for row in reader]
    return data

def analyze_data(data):
    sales = [sale for _, sale in data]
    return {
        'total': sum(sales),
        'average': mean(sales),
        'max': max(sales),
        'min': min(sales),
        'count': len(sales)
    }

def generate_pdf(data, analysis, filename='report.pdf'):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 1 * inch, "Sales Report")

    c.setFont("Helvetica", 12)
    y = height - 1.5 * inch
    c.drawString(1 * inch, y, "Sales Data:")
    y -= 0.3 * inch

    for name, sale in data:
        c.drawString(1.2 * inch, y, f"{name}: ${sale:.2f}")
        y -= 0.25 * inch

    y -= 0.3 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y, "Summary:")
    y -= 0.25 * inch
    c.setFont("Helvetica", 12)
    for key, value in analysis.items():
        c.drawString(1.2 * inch, y, f"{key.capitalize()}: {value:.2f}" if isinstance(value, float) else f"{key.capitalize()}: {value}")
        y -= 0.25 * inch

    c.save()
    print(f"PDF report saved as '{filename}'")

if __name__ == '__main__':
    file_path = 'data.csv'
    data = read_data(file_path)
    analysis = analyze_data(data)
    generate_pdf(data, analysis)
