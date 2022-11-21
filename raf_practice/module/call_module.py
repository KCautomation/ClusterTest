import raf_practice.module.car_module as object
# from raf_practice.module.car_module import info
# from raf_practice.module import car_module




class callModule:
    def car_description(self):
        make = "bmw"
        model = "550i"
        object.info(make, model)


m = callModule()
m.car_description()

# class callModule:
#     def car_description(self):
#         make = "bmw"
#         model = "550i"
#         info(make, model)
#
#
# m = callModule()
# m.car_description()

# class callModule:
#     def car_description(self):
#         make = "bmw"
#         model = "550i"
#         car_module.info(make, model)
#
#
# m = callModule()
# m.car_description()
