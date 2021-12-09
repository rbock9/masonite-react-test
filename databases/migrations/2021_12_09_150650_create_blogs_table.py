"""CreateBlogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateBlogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id")
            table.timestamps()
            table.string("mealname")
            table.string("image")
            table.string("rating")
            table.string("restaurant")
            table.string("restaurantaddress")
            table.string("summary")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")
