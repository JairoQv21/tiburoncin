class ProductCategory:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description

    def update_category(self, name, description):
        # Implement category update logic here
        self.name = name
        self.description = description
