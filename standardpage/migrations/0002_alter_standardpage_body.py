# Generated by Django 5.0.7 on 2024-08-17 13:13

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standardpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', 0), ('text', 1), ('document', 2), ('page', 3), ('info', 4), ('faq', 5), ('carousel', 9), ('image', 10), ('embed', 11), ('code', 14), ('blockquote', 15), ('quotation', 17), ('call_to_action_1', 21)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {}), 1: ('blocks.blocks.TextBlock', (), {}), 2: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 3: ('wagtail.blocks.PageChooserBlock', (), {'required': False}), 4: ('blocks.blocks.InfoBlock', (), {}), 5: ('blocks.blocks.FAQListBlock', (), {}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 7: ('wagtail.blocks.TextBlock', (), {}), 8: ('wagtail.blocks.StructBlock', [[('text', 7), ('author', 7)]], {}), 9: ('wagtail.blocks.StreamBlock', [[('image', 6), ('quotation', 8)]], {}), 10: ('blocks.blocks.ImageBlock', (), {}), 11: ('wagtail.embeds.blocks.EmbedBlock', (), {}), 12: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], 'help_text': 'Coding language', 'identifier': 'language', 'label': 'Language'}), 13: ('wagtail.blocks.TextBlock', (), {'identifier': 'code', 'label': 'Code'}), 14: ('wagtail.blocks.StructBlock', [[('language', 12), ('code', 13)]], {}), 15: ('wagtail.blocks.BlockQuoteBlock', (), {}), 16: ('wagtail.blocks.TextBlock', (), {'required': False}), 17: ('wagtail.blocks.StructBlock', [[('quote', 0), ('cite', 16)]], {'icon': 'openquote', 'template': 'blocks/blockquote.html'}), 18: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic'], 'required': True}), 19: ('wagtail.blocks.PageChooserBlock', (), {}), 20: ('wagtail.blocks.CharBlock', (), {'max_length': 100, 'required': False}), 21: ('wagtail.blocks.StructBlock', [[('text', 18), ('page', 19), ('button_text', 20)]], {})}, null=True),
        ),
    ]
