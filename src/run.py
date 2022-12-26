from generators import model_generator

md = model_generator.ModelGenerator("Test", "test")
md.handler()
md.save()