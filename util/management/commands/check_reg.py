import re

from django.core.management.base import BaseCommand, CommandError

from FaraData.models import Registrant, Client, Payment, Contact, Disbursement, Gift, Contribution


class Command(BaseCommand):
	def handle(self, pythonpath, verbosity, traceback, settings):
		wrong_contact = 0
		wrong_contribution = 0
		wrong_payment = 0 
		wrong_disbursement = 0
		problem_reg = []

		for contact in Contact.objects.all():
			reg_id = str(contact.registrant.reg_id)
			if reg_id not in contact.link:
				print "contact id", contact.id
				print reg_id, contact.link, contact.date, "\n"
				wrong_contact += 1
				if reg_id not in problem_reg:
					problem_reg.append(reg_id)
		print "%s wrong contacts" % (wrong_contact)
		
		for contribution in Contribution.objects.all():
			try:
				reg_id = str(contribution.registrant.reg_id)

				if reg_id not in contribution.link:
					print contribution.id
					print reg_id, contribution.link, contribution.date
					wrong_contribution += 1

					link = contribution.link
					real_reg_id = re.sub('-','', link[25:29])
					real_reg_id = re.sub('S','', real_reg_id)
					real_reg_id = re.sub('L','', real_reg_id)
					new_reg = Registrant(reg_id=real_reg_id)
					print "new_reg"
					contribution.registrant = new_reg
					contribution.save()
					print contribution.id

					if reg_id not in problem_reg:
						problem_reg.append(reg_id)
			except:
				print "error"
				bad_ids = [3375, 2579]
				link = contribution.link
				real_reg_id = re.sub('-','', link[25:29])
				real_reg_id = re.sub('S','', real_reg_id)
				real_reg_id = re.sub('L','', real_reg_id)
				if int(real_reg_id) not in bad_ids:
					new_reg = Registrant(reg_id=real_reg_id)
					print "new_reg", Registrant
				else:
					print "Why are you not fixed?", contribution.id

				print contribution.id
		print "%s wrong contributions" % (wrong_contribution)
		
		for payment in Payment.objects.all():
			reg_id = str(payment.registrant.reg_id)
			if reg_id not in payment.link:
				print "payment id ", payment.id
				print reg_id, payment.link, payment.date, "\n"
				wrong_payment += 1
				if reg_id not in problem_reg:
					problem_reg.append(reg_id)
		print "%s wrong payments " % (wrong_payment)

		for disbursement in Disbursement.objects.all():
			reg_id = str(disbursement.registrant.reg_id)
			if reg_id not in disbursement.link:
				print "dis id ", disbursement.id
				print reg_id, disbursement.link, disbursement.date, "\n"
				wrong_disbursement += 1
				if reg_id not in problem_reg:
					problem_reg.append(reg_id)
		print "%s wrong disbursements" % (wrong_disbursement)

		print "contact", wrong_contact
		print "contribution", wrong_contribution
		print "payment", wrong_payment
		print "bad registrants", problem_reg
