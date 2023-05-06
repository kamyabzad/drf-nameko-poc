# POC for creating a nameko wrapper around a DRF app

## Setting up the environment
1. Install the requirements:

`$ pip install -r requirements.txt`

2. Run the migrations.

`$ python manage.py migrate`

3. Create some Havij objects either through the django shell or through the rest API.

4. Start a RabbitMQ instance:

`$ docker run -d -p 5672:5672 rabbitmq:3`

5. Start the nameko services:

`$ DJANGO_SETTINGS_MODULE=rpcpoc.settings nameko run rpc`

Note the DJANGO_SETTINGS_MODULE environment variable.

6. You could test the result through nameko shell:

`$ nameko shell`

And then:

`>>> n.rpc.havij_wrapper.get()`
