fields = [
    {
        'field_name': 'name',
        'name': '药品名称',
        'extract_rule': '(?<=通用名称：)\w+'
    },
    {
        'field_name': 'ingredient',
        'name': '成份',
        'extract_rule': '(?<=【成份】).*'
    },
    {
        'field_name': 'character',
        'name': '性状',
        'extract_rule': '(?<=【性状】).*'
    },
    {
        'field_name': 'function',
        'name': '功能主治',
        'extract_rule': '(?<=【功能主治】).*'
    },
    {
        'field_name': 'indication',
        'name': '适应症',
        'extract_rule': '(?<=【适应症】).*'
    },
    {
        'field_name': 'usage',
        'name': '用法用量',
        'extract_rule': '(?<=【用法用量】).*'
    },
    {
        'field_name': 'adverse_effect',
        'name': '不良反应',
        'extract_rule': '(?<=【不良反应】).*'
    },
    {
        'field_name': 'contraindication',
        'name': '禁忌',
        'extract_rule': '(?<=【禁忌】).*'
    },
    {
        'field_name': 'warning',
        'name': '注意事项',
        'extract_rule': '(?<=【注意事项】).*'
    },
    {
        'field_name': 'pregnant',
        'name': '孕妇及哺乳期妇女用药',
        'extract_rule': '(?<=【孕妇及哺乳期妇女用药】).*'
    },
    {
        'field_name': 'children',
        'name': '儿童用药',
        'extract_rule': '(?<=【儿童用药】).*'
    },
    {
        'field_name': 'old',
        'name': '老年用药',
        'extract_rule': '(?<=【老年用药】).*'
    },
    {
        'field_name': 'storage',
        'name': '贮藏',
        'extract_rule': '(?<=【贮藏】).*'
    },
    {
        'field_name': 'interaction',
        'name': '药物相互作用',
        'extract_rule': '(?<=【药物相互作用】).*'
    },
    {
        'field_name': 'overdose',
        'name': '药物过量',
        'extract_rule': '(?<=【药物过量】).*'
    },
    {
        'field_name': 'packaging',
        'name': '包装',
        'extract_rule': '(?<=【包装】).*'
    },
    {
        'field_name': 'indate',
        'name': '有效期',
        'extract_rule': '(?<=【有效期】).*'
    },
    {
        'field_name': 'specification',
        'name': '规格',
        'extract_rule': '(?<=【规格】).*'
    },
]