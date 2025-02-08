from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter",
    auto_offset_reset="earliest",
)


jokes_topic = app.topic(name="jokes", value_deserializer="json")

sdf = app.dataframe(topic=jokes_topic)


sdf.update(lambda massage: print(f"input massage: {massage}"))


sdf = sdf.apply(split_words, expand=True)


sdf.update(lambda words: print (f"output: {words}"))

sdf = sdf.apply("word").apply(lambda word: len(word))

if __name__=='__main__':
    app.run()