const MongoClient = require("mongodb").MongoClient;

const MONGO_URL = "mongodb+srv://usr:pswrd@penquenclstr.gtjt3.mongodb.net/learningMongo?retryWrites=true&w=majority";

MongoClient.connect(MONGO_URL, (err, db) => {
    if (err) {
        return console.log(err);
    }

    db.collection('notes').insertOne(
        {
            title: 'Hello MongoDB',
            text: 'Hopefully this works!'
        },
        function (err, res) {
            if (err) {
                db.close();
                return console.log(err);
            }
            db.close();
        }
    )
});
