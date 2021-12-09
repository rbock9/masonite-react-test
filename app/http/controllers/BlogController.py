""" A BlogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Blog import Blog


class BlogController(Controller):
    
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Blog.where("id", id).get()

    def index(self):
        return Blog.all()

    def create(self):
        mealname = self.request.input("mealname")
        image = self.request.input("image")
        rating = self.request.input("rating")
        restaurant = self.request.input("restaurant")
        restaurantaddress = self.request.input("restaurantaddress")
        summary = self.request.input("summary")
        blog = Blog.create({
            "mealname": mealname, 
            "image": image,
            "rating": rating, 
            "restaurant": restaurant,
            "restaurantaddress": restaurantaddress, 
            "summary": summary
            })
        return blog

    def update(self):
        id = self.request.param("id")
        mealname = self.request.input("mealname")
        image = self.request.input("image")
        rating = self.request.input("rating")
        restaurant = self.request.input("restaurant")
        restaurantaddress = self.request.input("restaurantaddress")
        summary = self.request.input("summary")
        Blog.where("id", id).update({
            "mealname": mealname, 
            "image": image,
            "rating": rating, 
            "restaurant": restaurant,
            "restaurantaddress": restaurantaddress, 
            "summary": summary
            })
        return Blog.where("id", id).get()


    def destroy(self):
        id = self.request.param("id")
        blog = Blog.where("id", id).get()
        Blog.where("id", id).delete()
        return blog