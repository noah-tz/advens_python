from client import Client
from order import Order
import settings
from typing import Type
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class EmailSender:
    def __init__(self, sender_email: str, sender_password: str) -> None:
        self.sender_email = sender_email # "laundrythecity034@gmail.com"
        self.sender_password = sender_password # "xrqzlbpruagxljpr"

    def calling_the_server(self, to_email: str, text: str) -> None:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        server.sendmail(self.sender_email, to_email, text)
        server.quit()

    def create_msg(self, from_email: str, to_email: str, subject: str, body: str) -> str:
        msg = MIMEMultipart()    
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg.as_string()
    

    def password_recovery(self, client: Type[Client]) -> None:
        to_email = client.email
        text = self.create_msg(self.sender_email, to_email, "The city laundry - reset password for your account", f"The password for your account is-\n{client.password}\nSuccessfully")
        self.calling_the_server(to_email, text)

    def order_summary(self, order: Type[Order]) -> None:
        to_email = order.email_client
        body: str = "".join(f"{item}: {order.items[item]}.\n" for item in order.items)
        body += f"\ntotal order cost {order.calculate()}"
        text = self.create_msg(self.sender_email, to_email, f"order summary NO {order.NO}", body)
        self.calling_the_server(to_email, text)

    def Your_order_is_ready(self, order: Type[Order]) -> None:
        to_email = order.email_client
        text = self.create_msg(self.sender_email, to_email, f"The city laundry - order NO {order.NO}", "Your order is ready. You can get to the collection now\nSuccessfully")
        self.calling_the_server(to_email, text)

    def thank_you_email(self, order: Type[Order]) -> None:
        to_email = order.email_client
        text = self.create_msg(
                                self.sender_email,
                                to_email,
                                "The city laundry - reset password for your account",
                                f"The password for your account is-\n22\nSuccessfully",
        )
        self.calling_the_server(to_email, text)

    

cl = Client("0527184022", "noah", "t0527184022@gmail.com", "miryam hanevia 1", "1234")
orde = Order(cl.email, "4242")
orde.items = {"shirt": 4, "pants": 6, "tank top": 2}
se = EmailSender("laundrythecity034@gmail.com", "xrqzlbpruagxljpr")
# se.password_recovery(cl)
se.order_summary(orde)




