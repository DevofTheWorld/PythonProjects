from Classes import Ticekts_Method

def main():
    customer = []
    customer_type = []
    customer_fare = []

    p = Ticekts_Method()

    for i in range(2):
        customer.append(p.ask_name())
        customer_type.append(p.ask_type())

        fare = p.calculate_fare(customer_type[i])
        customer_fare.append(fare)


    p.display_passenger(customer, customer_type, customer_fare)


if __name__ == '__main__':
    main()
