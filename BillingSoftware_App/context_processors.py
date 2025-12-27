from .models import Companies, Currency, DateFormat, Tax, CompanyLogo, Miscellaneous

def company_common_data(request):
    company = Companies.objects.first()
    currency = Currency.objects.filter(company=company).first()
    date_format = DateFormat.objects.filter(company=company).first()
    tax = Tax.objects.filter(company=company).first()
    logo = CompanyLogo.objects.filter(company=company).first()

    # ✅ Use the default miscellaneous settings
    misc = Miscellaneous.objects.filter(is_default=True).first()
    confirm_logout = misc.confirmation if misc else False
    theme_color = misc.menu_color if misc and misc.menu_color else "win7"  # fallback to default

    return {
        'company': company,
        'currency': currency,
        'date_format': date_format,
        'tax': tax,
        'logo': logo,
        'confirm_logout': confirm_logout,
        'theme_color': theme_color,  # ✅ pass to template
    }
