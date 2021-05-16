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
            return city_with_no_hash
        else:
            return city

    def find_place(self, messages):
        
        for x in messages.split():

            # replace all punctuations with spaces
            replace_table = str.maketrans(string.punctuation, " "*len(string.punctuation))
            y = x.lower().translate(replace_table)

            # if there is a space in the beginning due to hash tag
            if y[1:] in self.list_of_places:
                return y[1:]

            # if there is a space at the end due to comma
            elif y[:-1] in self.list_of_places:
                return y[:-1]

            # if there is no space in the beginning
            elif y in self.list_of_places:
                return y

            # else return nothing
            else:
                pass
                