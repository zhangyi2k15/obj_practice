#!/usr/bin/env python
# encoding: utf-8
"""
@project: obj_practice
#@ide: PyCharm
@author: zhh
@license: (C) Copyright, ZHH individual Limited.
@contact: zhangyi2k15@qq.com
@software: python
@file: case_learn_3.py
@time: 2020/2/2 10:29 下午
@desc:
"""

class Property:
    def __init__(self, square_feet='', bed='', bath='', **kwargs):
        # super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = bed
        self.num_baths = bath

    def display(self):
        print('property details')
        print('==============')
        print('square feet:'.format(self.num_bedrooms))
        print(f'bathrooms: {self.num_baths}')
        print()

    @staticmethod
    def prompt_init():
        return dict(square_feet=input('enter the square feet: '),
                    beds=input('enter number of bedrooms: '),
                    bath=input('enter number of bathrooms: ')
                    )


class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print('apartment details')
        print(f'laundry: {self.laundry}')
        print(f'balcony: {self.balcony}')

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        # laundry = ''
        # while laundry.lower() not in Apartment.valid_laundries:
        #     laundry = input('what laundry facilities does '
        #                     'the property have ? ({})'.format(", ").join(Apartment.valid_laundries))
        # balcony = ''
        # while balcony.lower() not in Apartment.valid_balconies:
        #     balcony = input('Does the property have a balcony ? ({})'
        #                     .format(", ").join(Apartment.valid_balconies))
        laundry = get_valid_input('what laundry facilities does the property have ?',
                                  Apartment.valid_laundries)
        balcony = get_valid_input('Does the property have a balcony ?',
                                  Apartment.valid_balconies)

        parent_init.update({'laundry': laundry,
                            'balcony': balcony}
                           )
        return parent_init


def get_valid_input(input_string, valid_options):
    input_string += '({})'.format(', '.join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)

    return response


class House(Property):
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print('house details')
        print(f'# of stories: {self.num_stories}')
        print(f' garage: {self.garage}')
        print(f' fenced: {self.fenced}')

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input('is the yard fenced ?',
                                 House.valid_fenced)
        garage = get_valid_input('is there a garage ?',
                                 House.valid_garage)
        num_stories = input('how many stories ?')

        parent_init.update({'fenced': fenced,
                            'garage': garage,
                            'num_stories': num_stories}
                           )

        return parent_init


class Purchase(object):
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print('purchase details')
        print(f'selling price: {self.price}')
        print(f'estimated taxes {self.taxes}')

    @staticmethod
    def prompt_init():
        return dict(price=input('what is the selling price ?'),
                    taxe=input('what are the estimated taxes ?')
                    )


class Rental(object):
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print('rental detail')
        print(f'rent: {self.rent}')
        print(f'estimated utilities: {self.utilities}')
        print(f'furnished: {self.furnished}')

    @staticmethod
    def prompt_init():
        return dict(
            rent=input('what is the monthly rent ?'),
            utilities=input('what are the estimated utilities ?'),
            furnished=get_valid_input('is the property furnished ?', ('yes', 'no'))
        )


class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())

        return init


class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())

        return init


class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())

        return init


class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())

        return init


class Agent(object):
    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase
    }
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input(
            'what type of property? ',
            ('house', 'apartment')
        ).lower()
        payment_type = get_valid_input(
            'what payment types? ',
            ('purchase', 'rental')
        ).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))


if __name__ == '__main__':
    agent = Agent()
    agent.add_property()
