def address(city):
    """The function returns true if the passed argument matches any place mentioned in the server"""
    list_of_places = ["andhra-pradesh", "assam", "bihar", "chattisgarh", "gujarat", "goa", "haryana",
                      "himachal-pradesh",
                      "jammu-and-kashmir", "jharkhand", "maharashtra", "karnataka", "kerala", "madhya-pradesh",
                      "orissa",
                      "punjab", "rajasthan", "telangana", "tamil-nadu", "tripura", "uttar-pradesh", "uttarakhand",
                      "west-bengal", "manipur", "arunachal-pradesh", "agra", "ahmedabad", "aurangabad",
                      "ayodhya-and-mathura", "bengaluru", "bhopal", "bhubaneshwar", "chennai", "chandigarh-tricity",
                      "dadra-and-nagar-haveli", "dehra-dun", "ghaziabad", "hyderabad", "indore", "jaipur", "jammu",
                      "kanpur", "kolkata", "kota", "lucknow", "mumbai", "nagpur", "nashik", "new-delhi-ncr", "pune",
                      "patna", "prayagraj_allahbad", "ranchi", "raipur", "sonipat", "surat", "vadodra-baroda",
                      "varanasi",
                      "amritsar", "aligarh"]

    city_with_no_hash = city[1:]
    if city_with_no_hash in list_of_places:
        return True
    else:
        return False


