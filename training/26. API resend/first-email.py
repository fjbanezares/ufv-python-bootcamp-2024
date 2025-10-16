import resend

resend.api_key = "xxx"

r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "fjbanezares@gmail.com",
    "subject": "Hello World",
    "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
