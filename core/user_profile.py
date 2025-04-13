import hashlib
class UserProfile:
    def __init__(self,username, email, password, currency='US',locale='en_US'):
        self.username=username
        self.email=email
        self.password=self.hash_password(password)
        self.currency=currency
        self.locale=locale
        self.preferences = {}  
        self.security_settings={"two_factor_enabled": False}
        
       
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authentication(self,password):
        return self.password==self.hash_password(password)
    
    def change_password(self,new_password):
        self.password=self.hash_password(new_password)
    
    def update_preferecnces(self,theme=None, notifications_enabled=None):
        if theme:
            self.preferences['theme']=theme
        if notifications_enabled:
            self.preferences['notification_enabled']=notifications_enabled
    def enable_2fa(self):
        self.security_settings["two_factor_enabled"] = True

    def disable_2fa(self):
        self.security_settings["two_factor_enabled"] = False

    def set_currency(self,currency):
        self.currency=currency
    def set_locale(self,locale):
        self.locale=locale
        
    def get_user_data(self):
        return{
            "username": self.username,
            "email": self.email,
            "currency": self.currency,
            "locale": self.locale,
            "preferences": self.preferences,
            "security_settings": self.security_settings
        }