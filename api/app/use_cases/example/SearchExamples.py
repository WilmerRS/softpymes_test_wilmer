from app.models import ExampleModel


class SearchExamples:
    _model = ExampleModel()

    def __init__(self):
        pass

    def get(self, page, per_page, query):
        search = ExampleModel.name.like(f'{query}%')
        if not query:
            examples = self._model.query.paginate(page, per_page, error_out=False)
        else:
            examples = self._model.query.filter(search).paginate(page, per_page, error_out=False)

        result = []
        for example in examples.items:
            data = example.export_data()
            data['has_prev'] = examples.has_prev
            data['has_next'] = examples.has_next
            data['page'] = examples.page
            data['next_page'] = examples.page + 1 if examples.has_next else 0
            data['count_pages'] = examples.pages
            result.append(data)

        return result
