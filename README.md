# SendGrid CLI
Porting mandrill to sendgrid migration tool.

## How to install
1. `brew install python@3.9`
1. `python3 -m venv ~/Envs/sendgrid_venv`
1. `source ~/Envs/sendgrid_venv/bin/activate`
1. `pip install -r requirements.txt`

## How it's working
There's an SDK folder with sdk.py file, it's pretty much self explained just
select a command and run it.

## Usage
Please add a new environment variable called `SENDGRID_API_KEY_PRODUCTION` to
your bash.rc or one time to your terminal:
```
export SENDGRID_API_KEY_PRODUCTION='<your api key root key>'
```

## Example
```
python main.py --dest_subaccount <subaccount_exact_name> --add_sendgrid_users fake@gmail.com
```

### Note
Since each SendGrid sub account requires a unique email address you are
forced to add `+` to the email like this: `fake+foo@gmail.com`.
In case you don't add it, the code will add the subaccont name like this:
`fake+<sub_account_name>@gmail.com` => this is highly recommended.
