from graphene import Mutation
from graphene import String
from graphene_file_upload.scalars import Upload
from django.core.files.storage import FileSystemStorage

# Create your mutations here


class UploadFile(Mutation):
    ok = String()

    class Arguments:
        file_in = Upload(required=True)

    def mutate(self, info, file_in):
        file_system = FileSystemStorage()
        file_system.save(name=file_in.name, content=file_in)

        return UploadFile(ok=True)
