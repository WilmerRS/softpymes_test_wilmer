from app.models import ExampleModel


class CreateExamples:
    _model = ExampleModel()

    def __init__(self):
        pass

    def save(self, id, name, identification, description, status):
        _new_model = ExampleModel({id,
                                   name,
                                   identification,
                                   description,
                                   status}
                                  ).save()
        return _new_model.export_data()
