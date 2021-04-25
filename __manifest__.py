{
    'name' : 'TechWiki',
    'version' : '1.0',
    'sequence' : 1,
    'description' : 'Tech world info.',
    'depends' : ['contacts', 'sale'],
    'data' : [
        "views/tech_views.xml",
        "views/owner_views.xml",
        "views/foods_views.xml",
        "views/sales_description_views.xml",
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
