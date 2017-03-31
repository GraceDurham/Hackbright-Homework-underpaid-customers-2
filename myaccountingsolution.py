def find_over_under(text):
    melon_cost = 1.00
    the_file = open(text)

    for line in the_file:
        line = line.rstrip()
        line = line.split("|")
        customer_name = line[1]
        melon_count = float(line[2])
        customer_paid = float(line[3])
        # print customer_name, melon_count, customer_paid
        customer_expected_paid= float(melon_count) * float(melon_cost)
        # print customer_expected_paid


        if customer_paid > customer_expected_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected_paid)
            print "{} has overpaid for their melons".format(customer_name)

        elif customer_paid < customer_expected_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(customer_name, customer_paid, customer_expected_paid)
            print "{} has underpaid for their melons".format(customer_name)

        


find_over_under("customer-orders.txt")