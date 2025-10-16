import resend

resend.api_key = "re_D3G91yfU_Cq6AiB4MPR3JTTcfG927YAZ4"

r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "fjbanezares@gmail.com",
    "subject": "Hello World",
    "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
