---
title: Shoot a bullet through the system
date: 2021-06-10T19:37:38.262Z
thumb_image: /images/bullet.jpg
omit_header_text: "true"
draft: "false"
summary: Fail fast!
tags:
- Software Development
categories:
- Blogs
---

![](/images/software/bettersoftware/engineering/03-agilecreation/attachments/bullet.jpg)

Most cloud software architecture is layered - three or four layers, typically.

- The UI layer: This is the code users enter the system. If you use something like Angular, the UI layer itself may contain sub-layers like the HTML, the controller, and the services layers used to communicate with the backend microservices.

- The cloud backend later: This layer exposes a set of API's called by the UI layer. API implementations may be all consolidated in a single layer, or distributed across multiple microservices. In both cases, this is where a lot of the business logic of your application lies.

- The database layer: Most application will persist data in some form of SQL, or NoSQL database. It may also store frequently accessed data in cace, like redis.

*When starting off a new product, it should be your singular goal to get the team to build all the layers as quick as possible.*

The way to do this is to do the absolute minimum you can in a layer so you can activate the next one in the chain. You are aiming for a breadth first approach, keeping the depth in each of the layers to an absolute minimum.

This will ensure you surface up problems early on. You are, figuratively speaking, shooting a bullet through the solution to see if there are roadblocks. And you’re trying to do it as quick as a bullet travels. Well, almost! :)

For sure, problems will arise. How quickly you uncover is what is important here.

Note: There is one other activity that precedes this, in terms of priority - and that’s the plumbing. See “plumbing comes first.”
