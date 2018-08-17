import webapp2
import validate
import form
import cgi

form = form.form

def escapeHTML(string):
	return cgi.escape(string, quote=True)

class MainPage(webapp2.RequestHandler):
	def write_form(self, usernameerror="", passworderror="", verifyerror="", emailerror="", username="", password="", verify="", email=""):
		self.response.out.write(form % {"usernameerror": usernameerror,
										"passworderror": passworderror,
										"verifyerror": verifyerror,
										"emailerror": emailerror,
										"username": escapeHTML(username),
										"password": escapeHTML(password),
										"verify": escapeHTML(verify),
										"email": escapeHTML(str(email))})

	def get(self):
		# self.response.headers['Content-Type'] = 'text/html'
		self.write_form()

	def post(self):
		usernameerror=""
		passworderror=""
		verifyerror=""
		emailerror=""
		username = self.request.get('username')
		password = self.request.get('password')
		verify = self.request.get('verify')
		email = self.request.get('email')
		validUsername = validate.validUsername(username)
		validPassword = validate.validPassword(password)
		validVerify = validate.validVerify(verify,password)
		validEmail = validate.validEmail(email)

		if (validUsername and validPassword and validVerify and validEmail):			
			self.redirect("/success?username=" + username)
		else:
			if (not validUsername):
				usernameerror="That's not a valid username."
			if (not validPassword):
				passworderror="That wasn't a valid password."
			if (validPassword and not validVerify):
				verifyerror="Your passwords didn't match."
			if (not validEmail):
				emailerror="That's not a valid email."
			self.write_form(usernameerror=usernameerror,passworderror=passworderror,verifyerror=verifyerror,emailerror=emailerror,username=username,email=email)

class SuccessHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		self.response.out.write("<html><body> Welcome, %s!!! </body></html>" % username )

app = webapp2.WSGIApplication([('/',MainPage),('/success',SuccessHandler)], debug = True)		