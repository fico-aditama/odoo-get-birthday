from odoo import models, fields, api
from datetime import datetime, timedelta

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _compute_get_birthday(self):
        """
        Compute and set the start and end dates for the current week, last week, and next week.

        This method calculates the following for each record:
        - The start and end dates of the current week.
        - The start and end dates of the last week.
        - The start and end dates of the next week.

        The weeks are considered from Monday to Sunday.

        It assigns these calculated dates to the corresponding fields:
        - start_of_week
        - end_of_week
        - last_start_week
        - last_end_week
        - next_start_week
        - next_end_week
        """
        for record in self:
            today = datetime.today()  # Get today's date

            # Calculate the start of the current week (Monday)
            start_of_week = today - timedelta(days=today.weekday())

            # Calculate the end of the current week (Sunday)
            end_of_week = start_of_week + timedelta(days=6)

            # Set the current week's start and end dates
            record.start_of_week = start_of_week
            record.end_of_week = end_of_week

            # Calculate and set last week's start and end dates
            record.last_start_week = start_of_week - timedelta(days=7)  # Start of last week
            record.last_end_week = start_of_week - timedelta(days=1)  # End of last week

            # Calculate and set next week's start and end dates
            record.next_start_week = end_of_week + timedelta(days=1)  # Start of next week
            record.next_end_week = end_of_week + timedelta(days=7)  # End of next week

    # Define fields to store start and end dates of the current week
    start_of_week = fields.Datetime(string='Date Week Start', compute='_compute_get_birthday', store=True)
    end_of_week = fields.Datetime(string='Date Week End', compute='_compute_get_birthday', store=True)

    # Define fields to store start and end dates of the last week
    last_start_week = fields.Datetime(string='Date Last Week Start', compute='_compute_get_birthday', store=True)
    last_end_week = fields.Datetime(string='Date Last Week End', compute='_compute_get_birthday', store=True)

    # Define fields to store start and end dates of the next week
    next_start_week = fields.Datetime(string='Date Next Week Start', compute='_compute_get_birthday', store=True)
    next_end_week = fields.Datetime(string='Date Next Week End', compute='_compute_get_birthday', store=True)
