from odoo import models, fields, api
from datetime import datetime, timedelta
    
    
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _compute_get_birthday(self):
        for record in self:
            today = datetime.today()
            start_of_week = today - timedelta(days=today.weekday())  
            end_of_week = start_of_week + timedelta(days=6) 
        
            # Current Week
            record.start_of_week = start_of_week
            record.end_of_week = end_of_week

            # Last Week
            record.last_start_week = start_of_week - timedelta(days=7) 
            record.last_end_week = start_of_week - timedelta(days=1)

            # Next Week
            record.next_start_week = end_of_week + timedelta(days=1) 
            record.next_end_week = end_of_week + timedelta(days=7) 

    start_of_week = fields.Datetime(string='Date Week Start', compute='_compute_get_birthday', store=True)
    end_of_week = fields.Datetime(string='Date Week End', compute='_compute_get_birthday', store=True)

    last_start_week = fields.Datetime(string='Date Last Week Start', compute='_compute_get_birthday', store=True)
    last_end_week = fields.Datetime(string='Date Last Week End', compute='_compute_get_birthday', store=True)

    next_start_week = fields.Datetime(string='Date Next Week Start', compute='_compute_get_birthday', store=True)
    next_end_week = fields.Datetime(string='Date Next Week End', compute='_compute_get_birthday', store=True)
