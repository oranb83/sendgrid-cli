import os


SENDGRID_API_KEY_PRODUCTION = os.getenv('SENDGRID_API_KEY_PRODUCTION')
BASE_SCOPES = [
    'access_settings.activity.read',
    'access_settings.whitelist.read',
    'alerts.read',
    'asm.groups.read',
    'browsers.stats.read',
    'categories.create',
    'categories.delete',
    'categories.read',
    'categories.stats.read',
    'categories.stats.sums.read',
    'categories.update',
    'clients.desktop.stats.read',
    'clients.phone.stats.read',
    'clients.stats.read',
    'clients.tablet.stats.read',
    'clients.webmail.stats.read',
    'devices.stats.read',
    'email_testing.read',
    'email_testing.write',
    'geo.stats.read',
    'ips.pools.ips.read',
    'ips.pools.read',
    'ips.read',
    'ips.warmup.read',
    'mail.batch.read',
    'mail_settings.address_whitelist.read',
    'mail_settings.address_whitelist.update',
    'mail_settings.bcc.read',
    'mail_settings.bcc.update',
    'mail_settings.bounce_purge.read',
    'mail_settings.bounce_purge.update',
    'mail_settings.footer.read',
    'mail_settings.footer.update',
    'mail_settings.forward_bounce.read',
    'mail_settings.forward_bounce.update',
    'mail_settings.forward_spam.read',
    'mail_settings.forward_spam.update',
    'mail_settings.plain_content.read',
    'mail_settings.plain_content.update',
    'mail_settings.spam_check.read',
    'mail_settings.spam_check.update',
    'mail_settings.template.read',
    'mail_settings.template.update',
    'mailbox_providers.stats.read',
    'stats.global.read',
    'stats.read',
    'suppression.read',
    'templates.create',
    'templates.delete',
    'templates.read',
    'templates.update',
    'templates.versions.activate.create',
    'templates.versions.create',
    'templates.versions.delete',
    'templates.versions.read',
    'templates.versions.update',
    'tracking_settings.click.read',
    'tracking_settings.google_analytics.read',
    'tracking_settings.open.read',
    'tracking_settings.subscription.read',
    'user.scheduled_sends.read',
    'user.settings.enforced_tls.read',
    'user.timezone.read',
    'user.webhooks.event.settings.read',
    'user.webhooks.event.settings.update',
    'user.webhooks.event.test.create',
    'user.webhooks.event.test.read',
    'user.webhooks.event.test.update',
    'user.webhooks.parse.settings.read',
    'user.webhooks.parse.stats.read'
]
