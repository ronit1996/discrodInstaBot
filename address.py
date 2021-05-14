import textwrap
import string

class Address:
    list_of_places = ["andhra pradesh", "assam", "bihar", "chattisgarh", "gujarat", "goa", "haryana",
                      "himachal pradesh",
                      "jammu and kashmir", "jharkhand", "maharashtra", "karnataka", "kerala", "madhya pradesh",
                      "orissa",
                      "punjab", "rajasthan", "telangana", "tamil nadu", "tripura", "uttar pradesh", "uttarakhand",
                      "west bengal", "manipur", "arunachal pradesh", "agra", "ahmedabad", "aurangabad",
                      "ayodhya and mathura", "bengaluru", "bhopal", "bhubaneshwar", "chennai", "chandigarh tricity",
                      "dadra and nagar haveli", "dehra dun", "ghaziabad", "hyderabad", "indore", "jaipur", "jammu",
                      "kanpur", "kolkata", "kota", "lucknow", "mumbai", "nagpur", "nashik", "new delhi ncr", "pune",
                      "patna", "prayagraj allahbad", "ranchi", "raipur", "sonipat", "surat", "vadodra baroda",
                      "varanasi", "amritsar", "aligarh", "delhi", "gurgaon", "gurugram", "noida", "rishikesh", "delhincr", "dwarka"]

    def hash_address(self, city):
        """matches the tagged city with the cities list and removes the hash"""
        replace_table = str.maketrans(string.punctuation, " "*len(string.punctuation))
        city_with_no_hash = city[1:].translate(replace_table)
        if city_with_no_hash in self.list_of_places:
            return True
        else:
            return False

    def find_place(self, messages):
        replace_table = str.maketrans(string.punctuation, " "*len(string.punctuation))
        for x in messages.split():
            if x.lower().translate(replace_table) in self.list_of_places:
                return x
            else:
                pass


