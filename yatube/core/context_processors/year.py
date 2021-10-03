import datetime


def year(request):
    year = datetime.datetime.now().year
    return {'year': year}
