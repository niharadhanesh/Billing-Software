from django.urls import path,re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [
    path('',views.index,name='index'),
    path('Log_in/',views.Log_in,name='Log_in'),
    path('Fun_login/',views.Fun_login,name='Fun_login'),
    path('adminDashboard/',views.adminDashboard,name='adminDashboard'),
    path('admin_settings/',views.admin_settings,name='admin_settings'),
    path('LogOut/',views.LogOut,name='LogOut'),
    path('add_user/',views.add_user,name='add_user'),
    path('update_user_profile/<int:user_id>/',views.update_user_profile,name='update_user_profile'),
    path('delete_user/<int:user_id>/',views.delete_user,name='delete_user'),
    path('company_settings/',views.company_settings,name='company_settings'),
    path('add_company/',views.add_company,name='add_company'),
    path('edit_company/<int:company_id>/',views.edit_company,name='edit_company'),
    path('advanced_settings/',views.advanced_settings,name='advanced_settings'),
    path('advanced_template_settings/',views.advanced_template_settings,name='advanced_template_settings'),
    path('restore_template_defaults/',views.restore_template_defaults,name='restore_template_defaults'),

    #USER

    path('userDashboard/',views.userDashboard,name='userDashboard'),
    path('user_settings/',views.user_settings,name='user_settings'),
    path('user_advanced_settings/',views.user_advanced_settings,name='user_advanced_settings'),
    path('user_add_company/',views.user_add_company,name='user_add_company'),
    path('user_edit_company/<int:company_id>/',views.user_edit_company,name='user_edit_company'),
    path('user_advanced_template_settings/',views.user_advanced_template_settings,name='user_advanced_template_settings'),
    path('user_restore_template_defaults/',views.user_restore_template_defaults,name='user_restore_template_defaults'),

    path('miscellaneous_settings/',views.miscellaneous_settings,name='miscellaneous_settings'),
    path('create_default_extra_costs/',views.create_default_extra_costs,name='create_default_extra_costs'),
    path('add_new_cost/',views.add_new_cost,name='add_new_cost'),
    path('edit_cost/<int:cost_id>/',views.edit_cost,name='edit_cost'),
    path('delete_cost/<int:cost_id>/',views.delete_cost,name='delete_cost'),
    path('create_default_predefined_text/',views.create_default_predefined_text,name='create_default_predefined_text'),
    path('add_new_predefined_text/',views.add_new_predefined_text,name='add_new_predefined_text'),
    path('edit_header_footer/<int:text_id>/',views.edit_header_footer,name='edit_header_footer'),
    path('delete_header_footer/<int:text_id>/',views.delete_header_footer,name='delete_header_footer'),
    path('validate-old-password/', views.validate_old_password, name='validate_old_password'),
    path('change_password/',views.change_password,name='change_password'),
    path('create_default_payment_terms/',views.create_default_payment_terms,name='create_default_payment_terms'),
    path('add_new_payment_terms/',views.add_new_payment_terms,name='add_new_payment_terms'),
    path('edit_payment_term/<int:term_id>/',views.edit_payment_term,name='edit_payment_term'),
    path('delete_payment_term/<int:term_id>/',views.delete_payment_term,name='delete_payment_term'),
    path('create_default_misc_settings/',views.create_default_misc_settings,name='create_default_misc_settings'),
    path('update_misc_settings/',views.update_misc_settings,name='update_misc_settings'),

    path('invoice_settings/',views.invoice_settings,name='invoice_settings'),
    path('create_default_invoice_settings/',views.create_default_invoice_settings,name='create_default_invoice_settings'),
    path('update_invoice_settings/',views.update_invoice_settings,name='update_invoice_settings'),
    path('restore_invoice_defaults/',views.restore_invoice_defaults,name='restore_invoice_defaults'),

    path('order_settings/',views.order_settings,name='order_settings'),
    path('update_order_settings/',views.update_order_settings,name='update_order_settings'),
    path('restore_order_defaults/',views.restore_order_defaults,name='restore_order_defaults'),

    path('estimate_settings/',views.estimate_settings,name='estimate_settings'),
    path('create_default_estimate_settings/',views.create_default_estimate_settings,name='create_default_estimate_settings'),
    path('update_estimate_settings/',views.update_estimate_settings,name='update_estimate_settings'),
    path('restore_estimate_defaults/',views.restore_estimate_defaults,name='restore_estimate_defaults'),

    path('purchase_order/',views.purchase_order,name='purchase_order'),
    path('update_purchase_order_settings/',views.update_purchase_order_settings,name='update_purchase_order_settings'),
    path('restore_purchase_order_defaults/',views.restore_purchase_order_defaults,name='restore_purchase_order_defaults'),

    path('user_miscellaneous_settings/',views.user_miscellaneous_settings,name='user_miscellaneous_settings'),
    path('user_add_new_cost/',views.user_add_new_cost,name='user_add_new_cost'),
    path('user_edit_cost/<int:cost_id>/',views.user_edit_cost,name='user_edit_cost'),
    path('user_delete_cost/<int:cost_id>/',views.user_delete_cost,name='user_delete_cost'),
    path('user_add_new_predefined_text/',views.user_add_new_predefined_text,name='user_add_new_predefined_text'),
    path('user_edit_header_footer/<int:text_id>/',views.user_edit_header_footer,name='user_edit_header_footer'),
    path('user_delete_header_footer/<int:text_id>/',views.user_delete_header_footer,name='user_delete_header_footer'),
    path('user_add_new_payment_terms/',views.user_add_new_payment_terms,name='user_add_new_payment_terms'),
    path('user_edit_payment_term/<int:term_id>/',views.user_edit_payment_term,name='user_edit_payment_term'),
    path('user_delete_payment_term/<int:term_id>/',views.user_delete_payment_term,name='user_delete_payment_term'),
    path('user_update_misc_settings/',views.user_update_misc_settings,name='user_update_misc_settings'),

    path('user_invoice_settings/',views.user_invoice_settings,name='user_invoice_settings'),
    path('user_update_invoice_settings/',views.user_update_invoice_settings,name='user_update_invoice_settings'),
    path('user_restore_invoice_defaults/',views.user_restore_invoice_defaults,name='user_restore_invoice_defaults'),

    path('user_order_settings/',views.user_order_settings,name='user_order_settings'),
    path('user_update_order_settings/',views.user_update_order_settings,name='user_update_order_settings'),
    path('user_restore_order_defaults/',views.user_restore_order_defaults,name='user_restore_order_defaults'),

    path('user_estimate_settings/',views.user_estimate_settings,name='user_estimate_settings'),
    path('user_update_estimate_settings/',views.user_update_estimate_settings,name='user_update_estimate_settings'),
    path('user_restore_estimate_defaults/',views.user_restore_estimate_defaults,name='user_restore_estimate_defaults'),

    path('user_purchase_order/',views.user_purchase_order,name='user_purchase_order'),
    path('user_update_purchase_order_settings/',views.user_update_purchase_order_settings,name='user_update_purchase_order_settings'),
    path('user_restore_purchase_order_defaults/',views.user_restore_purchase_order_defaults,name='user_restore_purchase_order_defaults'),
    
    path('payment-settings/', views.payment_settings_view, name='payment_settings_view'),
    path('save-payment-settings/', views.save_payment_settings, name='save_payment_settings'),
    path('restore-paid-image/', views.restore_paid_image_default, name='restore_paid_image_default'),
    path('restore-payment-defaults/', views.restore_payment_defaults, name='restore_payment_defaults'),
 
    path('email-templates/', views.email_template_page, name='email_templates'),
    path('save-email-template/', views.save_email_template, name='save_email_template'),
    path('get-email-template/', views.get_email_template, name='get_email_template'),
    
    path('user-email-templates/', views.user_email_template_page, name='user_email_templates'),
    path('user-save-email-template/', views.user_save_email_template, name='user_save_email_template'),
    path('user-payment-settings/', views.user_payment_settings_view, name='user_payment_settings_view'),
    path('user-save-payment-settings/', views.user_save_payment_settings, name='user_save_payment_settings'),
    
    path('customer-list/', views.customer_list, name='customer_list'),
    path('get_tax_settings/', views.get_tax_settings, name='get_tax_settings'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('get_customer/<int:customer_id>/', views.get_customer, name='get_customer'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('api/categories/', views.get_categories, name='get_categories'),
    path('delete-customers/', views.delete_customers, name='delete_customers'),
    path('preview-invoice/', views.preview_invoice, name='preview_invoice'),
    path('email-invoice/', views.EmailInvoiceView.as_view(), name='email_invoice'),
    path('send-email-invoice/', views.send_email_invoice, name='send_email_invoice'),
    path('export-customers-excel/', views.export_customers_excel, name='export_customers_excel'),
    path('download-excel-template/', views.download_excel_template, name='download_excel_template'),
    path('import-customers/', views.import_customers_from_excel, name='import_customers_from_excel'),

    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)