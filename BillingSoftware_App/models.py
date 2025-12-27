from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Modules(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    create_invoice = models.BooleanField(default=True)
    delete_invoice = models.BooleanField(default=True)
    void_invoice = models.BooleanField(default=True)
    mark_invoice_as_paid = models.BooleanField(default=True)

    create_order = models.BooleanField(default=True)
    delete_order = models.BooleanField(default=True)

    create_estimate = models.BooleanField(default=True)
    delete_estimate = models.BooleanField(default=True)

    create_expense = models.BooleanField(default=True)
    delete_expense = models.BooleanField(default=True)

    turn_orders_into_invoices = models.BooleanField(default=True)
    turn_estimates_into_invoices = models.BooleanField(default=True)
    rebill_expenses = models.BooleanField(default=True)

    send_sms_notification = models.BooleanField(default=True)

    create_customer = models.BooleanField(default=True)
    delete_customer = models.BooleanField(default=True)
    import_customers = models.BooleanField(default=True)

    create_product_service = models.BooleanField(default=True)
    delete_product_service = models.BooleanField(default=True)
    import_products = models.BooleanField(default=True)

    run_reports = models.BooleanField(default=True)
    generate_recurring_invoices = models.BooleanField(default=True)

    create_purchase_order = models.BooleanField(default=True)
    delete_purchase_order = models.BooleanField(default=True)

    modify_invoice_settings = models.BooleanField(default=True)
    modify_order_settings = models.BooleanField(default=True)
    modify_estimate_settings = models.BooleanField(default=True)

    def __str__(self):
        return f"Permissions for {self.user.username}"


class Companies(models.Model):
    company_name = models.CharField(max_length=255,null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)
    sales_tax_reg_no = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.company_name


class Currency(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    currency_name = models.CharField(max_length=50,null=True)
    currency_sign = models.CharField(max_length=10,null=True)
    currency_sign_placement = models.CharField(max_length=20,null=True) 
    decimal_separator = models.CharField(max_length=5,null=True)

    def __str__(self):
        return f"{self.currency_name} for {self.company.company_name}"    
    


class DateFormat(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    format = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.format} - {self.company.company_name}"
    


class Tax(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    tax_type_first = models.CharField(max_length=50, null=True, blank=True)  
    tax1_name = models.CharField(max_length=100, null=True, blank=True)
    tax_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tax2_name = models.CharField(max_length=100, null=True, blank=True)
    tax2_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    print_tax1 = models.BooleanField(default=False)
    print_tax2 = models.BooleanField(default=False)
    tax_type_second = models.CharField(max_length=100, null=True, blank=True)
  
    def __str__(self):
        return f"Tax settings for {self.company.company_name}"
    


class CompanyLogo(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    image = models.FileField(upload_to='company_logos/',null=True,blank=True)
    print = models.BooleanField(default=False)

    def __str__(self):
        return f"Logo for {self.company.company_name}"


class Template(models.Model):
    template_name = models.CharField(max_length=255,null=True)
    page_size = models.CharField(max_length=100,null=True)
    right_margin_mm = models.IntegerField(null=True)
    invoice_block_shift_left_mm =models.IntegerField(null=True)
    invoice_block_shift_top_mm = models.IntegerField(null=True)



class PaymentTerms(models.Model):
    term_name = models.CharField(max_length=255,null=True)
    days = models.IntegerField(null=True)

    def __str__(self):
        return self.term_name


class ExtraCostList(models.Model):
    cost_name = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.cost_name


class PredefinedText(models.Model):
    predefined_text = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.predefined_text


class Miscellaneous(models.Model):
    menu_color = models.CharField(max_length=100,null=True)
    attachment_type = models.CharField(max_length=100,null=True)
    invoice_numbering = models.BooleanField(default=True)
    order_numbering = models.BooleanField(default=True)
    estimate_numbering = models.BooleanField(default=True)
    porder_numbering = models.BooleanField(default=True)
    confirmation = models.BooleanField(default=True)

    is_default = models.BooleanField(default=False)


    def __str__(self):
        return f"Miscellaneous Settings #{self.pk}"



class InvoiceSettings(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True, related_name='invoice_settings')

    invoice_number_prefix = models.CharField(max_length=50, default='INV',null=True)
    invoice_starting_number = models.IntegerField(default=1,null=True)
    header_background_color = models.CharField(max_length=50, default='#ffa500',null=True)  

    invoice_label = models.CharField(max_length=100, default='Invoice',null=True)
    invoice_number_label = models.CharField(max_length=100, default='Invoice #',null=True)
    invoice_date_label = models.CharField(max_length=100, default='Invoice Date',null=True)
    due_date_label = models.CharField(max_length=100, default='Due Date',null=True)
    order_ref_label = models.CharField(max_length=100, default='Order #',null=True)
    terms_label = models.CharField(max_length=100, default='Terms',null=True)
    invoice_to_label = models.CharField(max_length=100, default='Invoice To',null=True)
    ship_to_label = models.CharField(max_length=100, default='Ship To',null=True)
    id_sku_label = models.CharField(max_length=100, default='ID/SKU',null=True)
    product_service_label = models.CharField(max_length=100, default='Product/Service',null=True)
    quantity_label = models.CharField(max_length=100, default='Quantity',null=True)
    description_label = models.CharField(max_length=100, default='Description',null=True)
    unit_price_label = models.CharField(max_length=100, default='Unit Price',null=True)
    price_label = models.CharField(max_length=100, default='Price',null=True)
    subtotal_label = models.CharField(max_length=100, default='Subtotal',null=True)
    discount_label = models.CharField(max_length=100, default='Discount',null=True)
    discount_rate = models.CharField(max_length=100, default='Discount Rate',null=True)
    tax1 = models.CharField("Tax 1", max_length=100, default='Tax 1',null=True)
    tax2 = models.CharField("Tax 2", max_length=100, default='Tax 2',null=True)
    invoice_total = models.CharField(max_length=100, default='Invoice Total',null=True)
    total_paid = models.CharField(max_length=100, default='Total Paid',null=True)
    balance = models.CharField(max_length=100, default='Balance',null=True)
    terms_and_conditions = models.CharField(max_length=100, default='Terms and Conditions',null=True)
    tax_exempted = models.CharField(max_length=100, default='Tax Exempted',null=True)
    page = models.CharField(max_length=100, default='Page',null=True)
    of = models.CharField(max_length=100, default='of',null=True)
    invoice_terms_footer = models.TextField(blank=True)

    def __str__(self):
        return f"Invoice Settings ({self.template.template_name if self.template else 'No Template'})"



class OrderSettings(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    order_number_prefix = models.CharField(max_length=50, blank=True, null=True)
    order_starting_number = models.IntegerField(default=1,null=True)
    header_background_color = models.CharField(max_length=20, blank=True, null=True)

    order_label = models.CharField(max_length=100, blank=True, null=True)
    order_number_label = models.CharField(max_length=100, blank=True, null=True)
    order_date_label = models.CharField(max_length=100, blank=True, null=True)
    due_date_label = models.CharField(max_length=100, blank=True, null=True)
    order_to = models.CharField(max_length=255, blank=True, null=True)
    order_total = models.CharField(max_length=100, blank=True, null=True)
    order_terms_footer = models.TextField(blank=True)

    def __str__(self):
        return f"{self.template.template_name} - Order Settings"
    

class EstimateSettings(models.Model):
    template_name = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='estimate_settings',null=True)
    estimate_number_prefix = models.CharField(max_length=20, blank=True, null=True)
    estimate_starting_number = models.IntegerField(default=1,null=True)
    header_background_color = models.CharField(max_length=20, blank=True, null=True)
    estimate_label = models.CharField(max_length=50, default='Estimate',null=True)
    estimate_number_label = models.CharField(max_length=50, default='Estimate Number',null=True)
    estimate_date_label = models.CharField(max_length=50, default='Estimate Date',null=True)
    due_date_label = models.CharField(max_length=50, default='Due Date',null=True)
    estimate_to = models.CharField(max_length=100, default='Estimate To',null=True)
    estimate_total = models.CharField(max_length=50, default='Estimate Total',null=True)
    estimate_terms_footer = models.TextField(blank=True)

    def __str__(self):
        return f"{self.template_name.template_name} Estimate Settings"
    


class PurchaseOrderSettings(models.Model):
    template_name = models.ForeignKey(Template, on_delete=models.CASCADE, null=True)

    porder_number_prefix = models.CharField(max_length=20, default="P.ORD", blank=True)
    porder_starting_number = models.IntegerField(default=1, null=True)

    header_background_color = models.CharField(max_length=20, default="#ffa500", blank=True)

    porder_label = models.CharField(max_length=50, default="Purchase Order", blank=True)
    porder_number_label = models.CharField(max_length=50, default="Purchase Order #", blank=True)
    porder_date_label = models.CharField(max_length=50, default="Purchase Order Date", blank=True)
    due_date_label = models.CharField(max_length=50, default="Due Date", blank=True)
    porder_to = models.CharField(max_length=50, default="Vendor", blank=True)
    delivery_to = models.CharField(max_length=50, default="Delivery To", blank=True)
    porder_total = models.CharField(max_length=50, default="Purchase Order Total", blank=True)

    porder_terms_footer = models.TextField(blank=True)

    def __str__(self):
        return f"{self.template_name.template_name} Purchase Order"

class PaymentSettings(models.Model):
   
    payment_receipt_label = models.CharField(max_length=100, default='Payment Receipt')
    payment_for_invoice_label = models.CharField(max_length=100, default='Payment for Invoice #')
    amount_received_from_label = models.CharField(max_length=100, default='Amount received from:')
    description_label = models.CharField(max_length=100, default='Description:')
    payment_received_in_label = models.CharField(max_length=100, default='Payment Received in:')
    payment_receipt_number_label = models.CharField(max_length=100, default='Payment Receipt #')
    payment_date_label = models.CharField(max_length=100, default='Payment Date:')
    payment_amount_label = models.CharField(max_length=100, default='Payment Amount:')
    total_amount_due_label = models.CharField(max_length=100, default='Total Amount Due')
    total_paid_label = models.CharField(max_length=100, default='Total Paid')
    balance_due_label = models.CharField(max_length=100, default='Balance Due')
    payment_receipt_prefix = models.CharField(max_length=20, default='RCPT')
    paid_image = models.ImageField(upload_to='payment_images/', blank=True, null=True)
    show_paid_on_fully_paid = models.BooleanField(default=False)
    send_receipt_email_after_payment = models.BooleanField(default=False)
    attach_invoice_to_receipt_email = models.BooleanField(default=False)

    def __str__(self):
        return "Payment Settings"

class EmailTemplate(models.Model):
    template_name = models.CharField(max_length=50, unique=True)
    body = RichTextField()
    html = RichTextField()


from django.db import models
from django.contrib.auth.models import User

class CustomerCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=50, unique=True)
    customer_category = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE) 
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    business_name = models.CharField(max_length=255)
    address = models.TextField()
    ship_to_name = models.CharField(max_length=255)
    shipping_address = models.TextField()
    contact_person = models.CharField(max_length=255)
    email_address = models.EmailField()
    telephone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20, blank=True, null=True)
    sms_mobile_number = models.CharField(max_length=20)
    ship_to_contact_person = models.CharField(max_length=255)
    ship_to_email_address = models.EmailField()
    ship_to_telephone_number = models.CharField(max_length=20)
    ship_to_fax_number = models.CharField(max_length=20, blank=True, null=True)
    tax_exempt = models.BooleanField(default=False)
    specific_tax1_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    specific_tax2_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    customer_type = models.CharField(max_length=10, choices=[('client', 'Client'), ('vendor', 'Vendor'), ('both', 'Both')])
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_id} - {self.business_name}"
    

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_to = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField()
    email = models.EmailField()
    sms_number = models.CharField(max_length=20)
    ship_to_name = models.CharField(max_length=255)
    ship_to_address = models.TextField()
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    due_check = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    terms = models.ForeignKey(PaymentTerms, on_delete=models.SET_NULL, null=True, blank=True)
    order_reference = models.CharField(max_length=255, blank=True)

    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    specific_tax1_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    specific_tax2_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    extra_cost_name = models.ForeignKey(ExtraCostList, on_delete=models.SET_NULL, null=True, blank=True)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    sales_person = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50, default='Draft')
    tax_exempted = models.BooleanField(default=False)
    emailed_on = models.DateTimeField(null=True, blank=True)
    printed_on = models.DateTimeField(null=True, blank=True)

    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
 

    recurring = models.BooleanField(default=False)
    recurring_period = models.IntegerField(null=True, blank=True)
    recurring_intervel = models.CharField(max_length=100, blank=True)
    next_invoice = models.DateField(null=True, blank=True)
    stop_recurring_after = models.BooleanField(default=False)
    stop_recurring_date = models.DateField(null=True, blank=True)

    comments = models.TextField(blank=True)
    terms_text = models.TextField(blank=True)
    private_notes = models.TextField(blank=True)

    title_head = models.CharField(max_length=255, blank=True)
    page_header_text = models.CharField(max_length=255, blank=True)
    footer_text = models.TextField(blank=True)


