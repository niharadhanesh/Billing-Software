from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Modules

@receiver(post_save, sender=User)
def create_modules_for_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        if not Modules.objects.filter(user=instance).exists():
            Modules.objects.create(
                user=instance,
                create_invoice=True,
                delete_invoice=True,
                void_invoice=True,
                mark_invoice_as_paid=True,
                create_order=True,
                delete_order=True,
                create_estimate=True,
                delete_estimate=True,
                create_expense=True,
                delete_expense=True,
                turn_orders_into_invoices=True,
                turn_estimates_into_invoices=True,
                rebill_expenses=True,
                send_sms_notification=True,
                create_customer=True,
                delete_customer=True,
                import_customers=True,
                create_product_service=True,
                delete_product_service=True,
                import_products=True,
                run_reports=True,
                generate_recurring_invoices=True,
                create_purchase_order=True,
                delete_purchase_order=True,
                modify_invoice_settings=True,
                modify_order_settings=True,
                modify_estimate_settings=True,
            )
