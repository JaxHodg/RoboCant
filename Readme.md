# RoboCan 🤖🗑️

RoboCan won the Best Use of CockroachDB (MLH) at TOHacks 2022 🏆

## Inspiration 🤔

Single-use bottles are one of the largest portions of waste in North America, while in the EU many countries use reusable bottles with deposits to incentivize returns. We wanted to implement an efficient version of this system using NFC tags to track bottle returns and automatic return stations that can either return bottles or recycle waste instantly. Our idea, RoboCan, can be split into 3 main features.

## How we built it 🛠️

<img src="https://cdn.discordapp.com/attachments/963622812248080434/988230542552092702/IMG_7971.png" alt="RoboCan" width="300" align="right">

1. The sorting system, uses an ultrasonic sensor to detect when an object was placed on the lid and an embedded NFC reader to determine if the object is eligible for a refund. If the object is a reusable utensil with an outstanding deposit, then it would be placed separately from the waste and kept safe until it can be reused. If the object is just a normal piece of waste then it can be moved into the general waste storage area.

2. The CockroachDB database then records when reusable bottles have been purchased and from whom a deposit was collected from. This cloud-based server then waits for the same NFC-tagged bottle to be returned and would return the deposit to the buyer once it has. This purchase and return data would also be used for analytics, so we can improve our system based on how it’s being used.

3. Finally, we all know people are lazy and that requiring special trash cans to return bottles is inconvenient. Fortunately, that's an idea of the past since RoboCan has an Arduino-powered drivetrain that can bring it anywhere in the world! With our project, reusing bottles has been made easier than ever.

## Challenges we ran into 🥊

One of the biggest challenges was setting up the data storage while maintaining proper security, good data storage practices, and also allowing us to potentially expand for the future. While it would have been simple to set up a basic local database to store everything we needed within the RoboCan, we ended up deciding to use the more advanced CockroachLabs database which gave us impressive latency while also allowing us to implement cloud-based features like analyzing statistics over the internet. We did run into several issues trying to connect the various sections of our project to the database, including issues with some npm modules. Fortunately, CockroachLabs had extensive documentation and the fact that they used the common Postgres standard was super helpful for debugging and working around issues.

Another challenge for us was running the servo motor on the lid. Since the servo motors we had only operated from 0 to 90 degrees, we needed to increase the range of motion Robocan could achieve so the lid could tip to either side, in other words, go from 0 to 180 degrees. To achieve this, we found a simple 1:2 ratio 3D printable gearbox on Thingiverse to do just this. Once we had installed this gearbox, and achieved the range of motion we needed we found ourselves in another predicament, the weight of the NFC reader and other parts of the lid was too much on the now lower torque servo and it was unable to drive the lid. To solve this problem, many heavy components were adjusted and moved off the lid so their excess weight would not get in the way of the servo. Additionally, the hole in which our shaft was mounted was enlarged to decrease the friction that would counteract the movement of the servo. With these two solutions, our lid could now sort between NFC cups and other random garbage or in our case cups without NFC tags.

## What we learned & Accomplishments 🌟
I think all members of our team learned a lot about the structure of a project, and how vital getting the minimum viable product done is. Additionally, on the more technical side, I think we all learned a lot about databases, how all the parts of our project need to mesh and connect together as one, and overall what it takes to bring a successful project to completion in a short time frame. We are extremely proud of the product we created. It completes all of the base features we were looking to create and succeeds in our goal of sorting reusable cups and trash.

## What's next for RoboCan ⏩
Over this project we developed a ML algorithm to find users on a camera frame with the intention of navigating to the people automatically. Unfortunately, due to time, we were never able to properly implement this and so the drivetrain only worked via an IR remote.

### Thanks for reading! (Have a nice day 👋)
