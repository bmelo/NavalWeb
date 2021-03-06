import json

nodes = [
    ['C558A0627C9446548B23254872701164','Z-5111502P',False],
    ['950CBDB068994C10963963131A751BE0','"24""-SW-B18H-002-"',True],
    ['25B5BA5E7AC644CD84276902327BA1E1','VALV-51115002',False],
    ['E374ECABE2014723B6F0ADEA1799FDB2','"24""-SW-B18H-002-"',True],
    ['A9FA7C4BC8D344628D783465E50257B8','"24""-SW-B18H-002-"',True],
    ['0EB9ED0ACCBE41BB9F7C370F617AC1BD','"24""-SW-B18H-002-"',True],
    ['B8C3707136DB4966A6E534E033F778B9','XV-5111524',False],
    ['E37DCB79E4C64F63B1C071BDAB87A408','"24""-SW-B18H-002-"',True],
    ['563C412FFA1D46D7AEF9F7844237B8BB','"24""-SW-B18H-214-"',True],
    ['D2D3BC7AE3804003BA9477122F7BF0A9','"24""-SW-B18H-214-"',True],
    ['AF238B33DA0341DE92CD067F8C37FC5B','"14""-SW-B18H-214-NI"',True],
    ['3EE2AA386F8A4DAC879D7C277D7D4511','"24""-SW-B18H-214-"',True],
    ['5F62BFB7075C42D8BB1B3F69B499950B','"24""-SW-B18H-214-"',True],
    ['7342DE6A53E44B92A347A0AEB63CBCF5','HV-5111522',False],
    ['EF49451ECDB448C0B57D27BB83FE3770','"24""-SW-B18H-214-"',True],
    ['BA6B12F71AF248C6A8B348428016513E','"24""-SW-B18H-214-"',True],
    ['152CF901785642D3B4D63C848387ADCC','HV-5111521',False],
    ['8E5A24D1DF5042F9871CE6CA08BE4E08','"24""-SW-B18H-214-"',True],
    ['51445719BBE2483FA8D2123C5875FA6E','"24""-SW-B18H-214-"',True],
    ['F93E75371BFC4E1ABAB40BAB51D7AB09','"24""-SW-B18H-214-"',True],
    ['B7534C996FA1415ABEEF017E1EF2CCC6','"24""-SW-B18H-214-"',True],
    ['A4B1B7995172457886655672603D53F2','"24""-SW-B18H-214-"',True],
    ['A54D5B633BFC4A429D19AC778D3F2371','"14""-SW-B14H-005-"',True],
    ['3B7B5F5CD4BE4A4D86BF814A9B006219','"14""-SW-B14H-005-"',True],
    ['ED84453A06814765A04087F85C8FC487','2858',False],
    ['9316319A4A064FB6AD5134AA4A8946A4','"24""-SW-B18H-214-"',True],
    ['438D83A3617149E99769717D0609552A','"24""-SW-B18H-214-"',True],
    ['F9B6779DBBEF4BFCBF00B0153DDA6737','"14""-SW-B14H-012-"',True],
    ['20BEB38A4EFC44BFB7B28A1286E68079','"14""-SW-B14H-012-"',True],
    ['CBC5067AA669438691F35A4D9F316F9A','"24""-SW-B18H-002-"',True],
    ['243FF371296D43A884A895695512F576','HV-5111518',False],
    ['3F8F323D51154B47895CD45E32E450E8','"24""-SW-B18H-214-"',True],
    ['E7DEC852EDE7499A85B00731DC6C81D2','"14""-SW-B14H-012-"',True],
    ['2FB7A19582A04DDD8A619AA2D47A103A','2862',False],
    ['B9DFA95A7F4D4AEDA956DC41FF4BBB7F','2862',False],
    ['6D477AC8D8A0468AB0C550741F6EA08A','"24""-SW-B18H-002-"',True],
    ['72A23EDDC7CE4CA0BDD772DAFD7E0721','"14""-SW-B14H-012-NI"',True],
    ['BB9000C0523A446C8D8EBF040001D9AE','"14""-SW-B14H-052-"',True],
    ['5E3A426B25DA4B27B535F6F875A04BDD','"14""-SW-B14H-052-"',True],
    ['4C4C0ADC37A049C98FB62A6486479B6B','"12""-SW-B14H-024-NI"',True],
    ['F1E19586B4EB45378E219222F23E81DE','"12""-SW-B14H-029-"',True],
    ['07512585EEC04D138DE172A265446EAB','"14""-SW-B18H-214-"',True],
    ['BA319CEB875042359D9CF4E97600F229','"14""-SW-B14H-052-"',True],
    ['3F2E00C45FE649EE8A71CA366285E8D5','"12""-SW-B14H-024-NI"',True],
    ['A0D1D209BAF4451D97A7638618323CB0','VALV-52415056',False],
    ['7105EC5097154D5FBB74C902FE0D5D80','"14""-SW-B14H-005-"',True],
    ['0FB3089039ED41EDA03910792A1B8295','"12""-SW-B14H-024-NI"',True],
    ['83162CF17B244AC28C013F6E18B7CFA1','"4""-SW-B18H-066-NI"',True],
    ['3C8F382CBAF3419DBDA398750DAE4BE9','PV-5241509',False],
    ['F44DD002B889453AABFEF91498951284','"24""-SW-B18H-214-"',True],
    ['A9823DCAB84C42AAB695B918988A4C9A','"4""-SW-B18H-066-NI"',True],
    ['0E579CC8A43B4041B5E5A423CD85C160','FT-5111501B',False],
    ['D844F8C3224A4DF38EBEAA9745ADB71B','"24""-SW-B18H-214-"',True],
    ['631B2AD3329F4AE6BA11CB2E9DC64772','VALV-52415024',False],
    ['7C0D6DBA5F4F4D7BB5AC44E6E1F3DF19','"24""-SW-B18H-214-"',True],
    ['3DDA4458A31B498CBCCB7E5AC18C6547','"12""-SW-B14H-024-NI"',True],
    ['5DE1C81C75C346CB93C7A801ECD9E507','"12""-SW-B14H-024-NI"',True],
    ['4F0C1930CB9F47DDB2ED9077D75D3A3A','"8""-SW-B14H-024-NI"',True],
    ['16EFA207185146CC88E262A6752CE04B','"12""-SW-B14H-024-NI"',True],
    ['53F3FFD225B34405BBB7B38C3FB3E69A','"10""-SW-B14H-065-NI"',True],
    ['6ED95448AA374A91961DC5436DCDF135','"4""-SW-B18H-066-NI"',True],
    ['663A89CCB54F4BE2B06F689ED00AAB8E','"24""-SW-B18H-214-"',True],
    ['3704867669F14CDDA29807FC40470AAD','"10""-SW-B14H-024-NI"',True],
    ['E46DE2C4256C40DFB236642B2F5EEE4D','"4""-SW-B18H-066-NI"',True],
    ['83D38D3BD9B1479698C567026326A13E','"4""-SW-B18H-066-NI"',True],
    ['BA41295AA3E444B7AF063D4AC1CEABCA','"12""-SW-B14H-029-"',True],
    ['C3B0074CAE714210BD2D341BBE9708DD','"24""-SW-B18H-002-"',True],
    ['C360C6A37CB84CA599B83A6A7053AB0A','"10""-SW-B14H-065-NI"',True],
    ['260932ACA0B8414B941E0C409671B8B7','"8""-SW-B14H-024-NI"',True],
    ['6F35FF9A2D2646C6866A91B8ACAF24CD','"4""-SW-B18H-066-NI"',True],
    ['183943A4A00649659B8A81AC8C23EABD','"14""-SW-B14H-028-"',True],
    ['CE35BFB23CFE4A7A906E587AEDF5FE4A','"10""-SW-B14H-024-NI"',True],
    ['B944808064D940B0987AA5D873B35CC1','"14""-SW-B14H-028-"',True],
    ['1382BE778C6B4F3B9F28B56FC340FB35','"12""-SW-B14H-029-"',True],
    ['72318B8E2F5A41A0B069E40E01923609','"4""-SW-B18H-066-NI"',True],
    ['18D89F8791EA4F2EA68BD481A283BB73','"24""-SW-B18H-214-"',True],
    ['6A2EDF8265E8421DBA33BB5E7580309E','B-5241502B',False],
    ['A62FC1BB82104D22A9E7CAAB5A0B5412','"4""-SW-B18H-066-NI"',True],
    ['7E235C3F8F704AC5AF5AF139FDC16E0A','"4""-SW-B18H-066-NI"',True],
    ['5F8D4187E4C04BAE944274D82E0CDC10','"12""-SW-B14H-029-"',True],
    ['9AEC07141E1E402294C417F8617551AB','"4""-SW-B18H-066-NI"',True],
    ['CBFB1B048330472DAB1CC97A2DA1C365','"4""-SW-B18H-066-NI"',True],
    ['12DEFD367DE64FC89A6B95B752E5AC12','"4""-SW-B18H-066-NI"',True],
    ['674920F505AD460DB6B02E89B1789491','"4""-SW-B14H-066-NI"',True],
    ['83614D8665FD4C919EBD168CD616E063','"12""-SW-B14H-024-NI"',True],
    ['86A00F581D284435BA1AE5EA9DDFB2E5','"12""-SW-B14H-024-NI"',True],
    ['7E4CDFE4292B4A6C98287BF7C126B689','GG-5241501A',False],
    ['ABE0388F75204DA082A420753D0E9B08','"12""-SW-B14H-024-"',True],
    ['C6030B1381D1470BB248F6DD606DBB90','"14""-SW-B14H-026-"',True],
    ['D23EA902EA884458ACCF8072D555CDE7','"24""-SW-B18H-214-"',True],
    ['BA88E57D668647579BF3016108E65EE5','"12""-SW-B14H-024-NI"',True],
    ['596952EFB1D34AA4BFCF64773AF50857','ESP-52415048',False],
    ['792D0312AE8E4A3DA16CA658179D38A2','"12""-SW-B14H-024-NI"',True],
    ['3E303AC1E30542B39391373EFC413239','"12""-SW-B14H-024-NI"',True],
    ['441B037684614EC581B4E02554E4E3CA','"24""-SW-B18H-214-"',True],
    ['BAF69E705DDF48AA877184E03C4BB52B','2872',False],
    ['3EF8F05BABDF40259EADC44131819AF0','2872',False],
    ['05B5F361E4CD4851AC3F2851660BA5D7','"14""-SW-B14H-028-"',True],
    ['E87EA9C0D1B346F98F4500A422FD4F87','"24""-SW-B18H-002-"',True],
    ['E2182343C50B4EFCBCF62A52C01469FA','"12""-SW-B14H-024-NI"',True],
    ['78B19E91F58E41CE8BF250D93F8CABF4','"12""-SW-B14H-024-"',True],
    ['E9BC66131EB24D9FBEA8881D28B25919','"12""-SW-B14H-029-"',True],
    ['39A7733B0D2047F88CB9A3E649B860A3','XV-5241549',False],
    ['537AEE5321A649DD8AEE2AA4F56EBA90','"12""-SW-B14H-029-"',True],
    ['B433C67E79B84FE0AE9A6C7B68C9BB3E','B-5241502A',False],
    ['3712D33E3E15451F9E2A0536EFB11BF5','"14""-SW-B14H-026-"',True],
    ['78EA39E83DDB4B419CEA0183172DD619','"14""-SW-B14H-026-"',True],
    ['288EFC7D9B254FD8B38C10660776FF9A','"14""-SW-B14H-026-"',True],
    ['3F0EDC302897422C88BA2269650C237B','HV-5111506',False],
    ['5F66565B3067499783317018B867B058','XV-5241547',False],
    ['F0DA3055BB1649A5832776B1042CEEFD','"14""-SW-B14H-026-"',True],
    ['096E69E3C6D44B4DB767D596AB8A2E09','2858',False],
    ['105705F450774C218EA05BBE90970FED','"14""-SW-B14H-052-"',True],
    ['308DB54064384D5F8769EAF223D56CE0','"14""-SW-B14H-005-"',True],
    ['B90913ACD9EB4181A2719EC49D7BE3DE','"14""-SW-B14H-052-"',True],
    ['B90643B8D5C043A681B0ACF230DF7CBC','"14""-SW-B14H-052-"',True],
    ['B8B7989D606A4B5BBFB28F6840986D17','"12""-SW-B14H-024-NI"',True],
    ['2595E28BB40447F1BDA5716D5CF2CF33','"12""-SW-B14H-024-"',True],
    ['2C2BB4952A044DCE96DBD2358BBC1911','"14""-SW-B14H-052-"',True],
    ['EB3F38B98ED9457BB0A1A697F65D14CD','"12""-SW-B14H-024-"',True],
    ['6A1CA6D29CD645058BF2E71637528693','XV-5241551',False],
    ['DA75F465071F4B0099024271E55BBB3C','"4""-SW-B18H-066-NI"',True],
    ['FF2A6FBDC9A8418BA7223752DD262C10','"12""-SW-B14H-024-"',True],
    ['47B23B0B0D2842EE81F10FBD51ACD595','"12""-SW-B14H-024-"',True],
    ['B27B64CAA71642DA90B540A0864BF58D','VALV-52415031',False],
    ['7C553E5F56F940089B25CC7F52A285CE','HV-5241524',False],
    ['C8AC0F7B15BB4296AAB0451CE54CE0C4','"12""-SW-B14H-024-NI"',True],
    ['A9A054CF690743A194A1370C128C92BF','"12""-SW-B14H-024-"',True],
    ['A9A8357A4A284F00964452E9BF83B9A2','"24""-SW-B18H-002-"',True],
    ['876D1314DD694C6E9E913D180DE8FEEB','"12""-SW-B14H-024-NI"',True],
    ['537D59BD3F004653B62DA5A6F78C5114','"14""-SW-B14H-028-"',True],
    ['EE01F70565174F28A16E3EE39DEFF941','"12""-SW-B14H-024-"',True],
    ['BC9B6CDF14A1452B843D9A1C6D28FB8A','"14""-SW-B14H-028-"',True],
    ['084CEBB7191E433FAC9D7E9F442FEAD5','XV-5241552',False],
    ['C3320AA78B5D4EAEB49F8E2B98A7A529','"12""-SW-B14H-024-NI"',True],
    ['715C7156BC9B4A4FAC8DE23C1C4BC329','"14""-SW-B14H-052-"',True]
]


edges = [
    ['C558A0627C9446548B23254872701164','950CBDB068994C10963963131A751BE0','Directed','Pipe',None],
    ['950CBDB068994C10963963131A751BE0','25B5BA5E7AC644CD84276902327BA1E1','Directed','Other','VA'],
    ['25B5BA5E7AC644CD84276902327BA1E1','E87EA9C0D1B346F98F4500A422FD4F87','Directed','Pipe',None],
    ['E374ECABE2014723B6F0ADEA1799FDB2','A9FA7C4BC8D344628D783465E50257B8','Directed','Pipe',None],
    ['A9FA7C4BC8D344628D783465E50257B8','0EB9ED0ACCBE41BB9F7C370F617AC1BD','Directed','Pipe',None],
    ['0EB9ED0ACCBE41BB9F7C370F617AC1BD','B8C3707136DB4966A6E534E033F778B9','Directed','Other','XV'],
    ['B8C3707136DB4966A6E534E033F778B9','6D477AC8D8A0468AB0C550741F6EA08A','Directed','Pipe',None],
    ['E37DCB79E4C64F63B1C071BDAB87A408','0E579CC8A43B4041B5E5A423CD85C160','Directed','Other','FT'],
    ['563C412FFA1D46D7AEF9F7844237B8BB','D23EA902EA884458ACCF8072D555CDE7','Directed','Pipe',None],
    ['D2D3BC7AE3804003BA9477122F7BF0A9','563C412FFA1D46D7AEF9F7844237B8BB','Directed','Pipe',None],
    ['D2D3BC7AE3804003BA9477122F7BF0A9','D23EA902EA884458ACCF8072D555CDE7','Directed','Pipe',None],
    ['AF238B33DA0341DE92CD067F8C37FC5B','F9B6779DBBEF4BFCBF00B0153DDA6737','Directed','Pipe',None],
    ['3EE2AA386F8A4DAC879D7C277D7D4511','5F62BFB7075C42D8BB1B3F69B499950B','Directed','Pipe',None],
    ['5F62BFB7075C42D8BB1B3F69B499950B','3F8F323D51154B47895CD45E32E450E8','Directed','Pipe',None],
    ['7342DE6A53E44B92A347A0AEB63CBCF5','BA6B12F71AF248C6A8B348428016513E','Directed','Pipe',None],
    ['EF49451ECDB448C0B57D27BB83FE3770','F44DD002B889453AABFEF91498951284','Directed','Pipe',None],
    ['BA6B12F71AF248C6A8B348428016513E','152CF901785642D3B4D63C848387ADCC','Directed','Other','HV'],
    ['152CF901785642D3B4D63C848387ADCC','441B037684614EC581B4E02554E4E3CA','Directed','Pipe',None],
    ['8E5A24D1DF5042F9871CE6CA08BE4E08','7342DE6A53E44B92A347A0AEB63CBCF5','Directed','Other','HV'],
    ['51445719BBE2483FA8D2123C5875FA6E','F93E75371BFC4E1ABAB40BAB51D7AB09','Directed','Pipe',None],
    ['F93E75371BFC4E1ABAB40BAB51D7AB09','7C0D6DBA5F4F4D7BB5AC44E6E1F3DF19','Directed','Pipe',None],
    ['B7534C996FA1415ABEEF017E1EF2CCC6','07512585EEC04D138DE172A265446EAB','Directed','Pipe',None],
    ['B7534C996FA1415ABEEF017E1EF2CCC6','A54D5B633BFC4A429D19AC778D3F2371','Directed','Pipe',None],
    ['A4B1B7995172457886655672603D53F2','B7534C996FA1415ABEEF017E1EF2CCC6','Directed','Pipe',None],
    ['A54D5B633BFC4A429D19AC778D3F2371','308DB54064384D5F8769EAF223D56CE0','Directed','Pipe',None],
    ['3B7B5F5CD4BE4A4D86BF814A9B006219','ED84453A06814765A04087F85C8FC487','Directed','Pipe',None],
    ['ED84453A06814765A04087F85C8FC487','096E69E3C6D44B4DB767D596AB8A2E09','Directed','Pipe',None],
    ['9316319A4A064FB6AD5134AA4A8946A4','AF238B33DA0341DE92CD067F8C37FC5B','Directed','Pipe',None],
    ['9316319A4A064FB6AD5134AA4A8946A4','438D83A3617149E99769717D0609552A','Directed','Pipe',None],
    ['9316319A4A064FB6AD5134AA4A8946A4','F9B6779DBBEF4BFCBF00B0153DDA6737','Directed','Pipe',None],
    ['438D83A3617149E99769717D0609552A','18D89F8791EA4F2EA68BD481A283BB73','Directed','Pipe',None],
    ['F9B6779DBBEF4BFCBF00B0153DDA6737','20BEB38A4EFC44BFB7B28A1286E68079','Directed','Pipe',None],
    ['20BEB38A4EFC44BFB7B28A1286E68079','243FF371296D43A884A895695512F576','Directed','Other','HV'],
    ['CBC5067AA669438691F35A4D9F316F9A','E374ECABE2014723B6F0ADEA1799FDB2','Directed','Pipe',None],
    ['243FF371296D43A884A895695512F576','E7DEC852EDE7499A85B00731DC6C81D2','Directed','Pipe',None],
    ['3F8F323D51154B47895CD45E32E450E8','663A89CCB54F4BE2B06F689ED00AAB8E','Directed','Pipe',None],
    ['E7DEC852EDE7499A85B00731DC6C81D2','2FB7A19582A04DDD8A619AA2D47A103A','Directed','Pipe',None],
    ['2FB7A19582A04DDD8A619AA2D47A103A','B9DFA95A7F4D4AEDA956DC41FF4BBB7F','Directed','Pipe',None],
    ['B9DFA95A7F4D4AEDA956DC41FF4BBB7F','72A23EDDC7CE4CA0BDD772DAFD7E0721','Directed','Pipe',None],
    ['6D477AC8D8A0468AB0C550741F6EA08A','A9A8357A4A284F00964452E9BF83B9A2','Directed','Pipe',None],
    ['72A23EDDC7CE4CA0BDD772DAFD7E0721','2C2BB4952A044DCE96DBD2358BBC1911','Directed','Pipe',None],
    ['BB9000C0523A446C8D8EBF040001D9AE','7C553E5F56F940089B25CC7F52A285CE','Directed','Other','HV'],
    ['BB9000C0523A446C8D8EBF040001D9AE','BA319CEB875042359D9CF4E97600F229','Directed','Pipe',None],
    ['5E3A426B25DA4B27B535F6F875A04BDD','715C7156BC9B4A4FAC8DE23C1C4BC329','Directed','Pipe',None],
    ['4C4C0ADC37A049C98FB62A6486479B6B','C8AC0F7B15BB4296AAB0451CE54CE0C4','Directed','Pipe',None],
    ['F1E19586B4EB45378E219222F23E81DE','5F8D4187E4C04BAE944274D82E0CDC10','Directed','Pipe',None],
    ['07512585EEC04D138DE172A265446EAB','A54D5B633BFC4A429D19AC778D3F2371','Directed','Pipe',None],
    ['BA319CEB875042359D9CF4E97600F229','BB9000C0523A446C8D8EBF040001D9AE','Directed','Pipe',None],
    ['BA319CEB875042359D9CF4E97600F229','5E3A426B25DA4B27B535F6F875A04BDD','Directed','Pipe',None],
    ['3F2E00C45FE649EE8A71CA366285E8D5','C360C6A37CB84CA599B83A6A7053AB0A','Directed','Pipe',None],
    ['3F2E00C45FE649EE8A71CA366285E8D5','CE35BFB23CFE4A7A906E587AEDF5FE4A','Directed','Pipe',None],
    ['3F2E00C45FE649EE8A71CA366285E8D5','53F3FFD225B34405BBB7B38C3FB3E69A','Directed','Pipe',None],
    ['3F2E00C45FE649EE8A71CA366285E8D5','E2182343C50B4EFCBCF62A52C01469FA','Directed','Pipe',None],
    ['A0D1D209BAF4451D97A7638618323CB0','0FB3089039ED41EDA03910792A1B8295','Directed','Pipe',None],
    ['7105EC5097154D5FBB74C902FE0D5D80','BA319CEB875042359D9CF4E97600F229','Directed','Pipe',None],
    ['0FB3089039ED41EDA03910792A1B8295','260932ACA0B8414B941E0C409671B8B7','Directed','Pipe',None],
    ['83162CF17B244AC28C013F6E18B7CFA1','7E4CDFE4292B4A6C98287BF7C126B689','Directed','Other','GG'],
    ['3C8F382CBAF3419DBDA398750DAE4BE9','4F0C1930CB9F47DDB2ED9077D75D3A3A','Directed','Pipe',None],
    ['F44DD002B889453AABFEF91498951284','9316319A4A064FB6AD5134AA4A8946A4','Directed','Pipe',None],
    ['A9823DCAB84C42AAB695B918988A4C9A','A62FC1BB82104D22A9E7CAAB5A0B5412','Directed','Pipe',None],
    ['A9823DCAB84C42AAB695B918988A4C9A','83D38D3BD9B1479698C567026326A13E','Directed','Pipe',None],
    ['0E579CC8A43B4041B5E5A423CD85C160','D2D3BC7AE3804003BA9477122F7BF0A9','Directed','Pipe',None],
    ['D844F8C3224A4DF38EBEAA9745ADB71B','EF49451ECDB448C0B57D27BB83FE3770','Directed','Pipe',None],
    ['631B2AD3329F4AE6BA11CB2E9DC64772','1382BE778C6B4F3B9F28B56FC340FB35','Directed','Pipe',None],
    ['7C0D6DBA5F4F4D7BB5AC44E6E1F3DF19','A4B1B7995172457886655672603D53F2','Directed','Pipe',None],
    ['3DDA4458A31B498CBCCB7E5AC18C6547','83614D8665FD4C919EBD168CD616E063','Directed','Pipe',None],
    ['5DE1C81C75C346CB93C7A801ECD9E507','86A00F581D284435BA1AE5EA9DDFB2E5','Directed','Pipe',None],
    ['4F0C1930CB9F47DDB2ED9077D75D3A3A','3DDA4458A31B498CBCCB7E5AC18C6547','Directed','Pipe',None],
    ['16EFA207185146CC88E262A6752CE04B','4C4C0ADC37A049C98FB62A6486479B6B','Directed','Pipe',None],
    ['53F3FFD225B34405BBB7B38C3FB3E69A','7E4CDFE4292B4A6C98287BF7C126B689','Directed','Other','GG'],
    ['6ED95448AA374A91961DC5436DCDF135','72318B8E2F5A41A0B069E40E01923609','Directed','Pipe',None],
    ['6ED95448AA374A91961DC5436DCDF135','9AEC07141E1E402294C417F8617551AB','Directed','Pipe',None],
    ['6ED95448AA374A91961DC5436DCDF135','CBFB1B048330472DAB1CC97A2DA1C365','Directed','Pipe',None],
    ['663A89CCB54F4BE2B06F689ED00AAB8E','8E5A24D1DF5042F9871CE6CA08BE4E08','Directed','Pipe',None],
    ['3704867669F14CDDA29807FC40470AAD','7E4CDFE4292B4A6C98287BF7C126B689','Directed','Other','GG'],
    ['E46DE2C4256C40DFB236642B2F5EEE4D','A9823DCAB84C42AAB695B918988A4C9A','Directed','Pipe',None],
    ['83D38D3BD9B1479698C567026326A13E','7E4CDFE4292B4A6C98287BF7C126B689','Directed','Other','GG'],
    ['BA41295AA3E444B7AF063D4AC1CEABCA','631B2AD3329F4AE6BA11CB2E9DC64772','Directed','Other','VA'],
    ['C3B0074CAE714210BD2D341BBE9708DD','E37DCB79E4C64F63B1C071BDAB87A408','Directed','Pipe',None],
    ['C360C6A37CB84CA599B83A6A7053AB0A','53F3FFD225B34405BBB7B38C3FB3E69A','Directed','Pipe',None],
    ['260932ACA0B8414B941E0C409671B8B7','3C8F382CBAF3419DBDA398750DAE4BE9','Directed','Other','PV'],
    ['6F35FF9A2D2646C6866A91B8ACAF24CD','12DEFD367DE64FC89A6B95B752E5AC12','Directed','Pipe',None],
    ['183943A4A00649659B8A81AC8C23EABD','6A2EDF8265E8421DBA33BB5E7580309E','Directed','Other','B-'],
    ['CE35BFB23CFE4A7A906E587AEDF5FE4A','3704867669F14CDDA29807FC40470AAD','Directed','Pipe',None],
    ['B944808064D940B0987AA5D873B35CC1','05B5F361E4CD4851AC3F2851660BA5D7','Directed','Pipe',None],
    ['1382BE778C6B4F3B9F28B56FC340FB35','39A7733B0D2047F88CB9A3E649B860A3','Directed','Other','XV'],
    ['72318B8E2F5A41A0B069E40E01923609','7E4CDFE4292B4A6C98287BF7C126B689','Directed','Other','GG'],
    ['18D89F8791EA4F2EA68BD481A283BB73','3EE2AA386F8A4DAC879D7C277D7D4511','Directed','Pipe',None],
    ['6A2EDF8265E8421DBA33BB5E7580309E','EE01F70565174F28A16E3EE39DEFF941','Directed','Pipe',None],
    ['A62FC1BB82104D22A9E7CAAB5A0B5412','83D38D3BD9B1479698C567026326A13E','Directed','Pipe',None],
    ['7E235C3F8F704AC5AF5AF139FDC16E0A','83162CF17B244AC28C013F6E18B7CFA1','Directed','Pipe',None],
    ['5F8D4187E4C04BAE944274D82E0CDC10','537AEE5321A649DD8AEE2AA4F56EBA90','Directed','Pipe',None],
    ['9AEC07141E1E402294C417F8617551AB','DA75F465071F4B0099024271E55BBB3C','Directed','Pipe',None],
    ['CBFB1B048330472DAB1CC97A2DA1C365','72318B8E2F5A41A0B069E40E01923609','Directed','Pipe',None],
    ['12DEFD367DE64FC89A6B95B752E5AC12','6ED95448AA374A91961DC5436DCDF135','Directed','Pipe',None],
    ['674920F505AD460DB6B02E89B1789491','6F35FF9A2D2646C6866A91B8ACAF24CD','Directed','Pipe',None],
    ['83614D8665FD4C919EBD168CD616E063','5DE1C81C75C346CB93C7A801ECD9E507','Directed','Pipe',None],
    ['86A00F581D284435BA1AE5EA9DDFB2E5','876D1314DD694C6E9E913D180DE8FEEB','Directed','Pipe',None],
    ['86A00F581D284435BA1AE5EA9DDFB2E5','674920F505AD460DB6B02E89B1789491','Directed','Pipe',None],
    ['86A00F581D284435BA1AE5EA9DDFB2E5','6F35FF9A2D2646C6866A91B8ACAF24CD','Directed','Pipe',None],
    ['ABE0388F75204DA082A420753D0E9B08','FF2A6FBDC9A8418BA7223752DD262C10','Directed','Pipe',None],
    ['C6030B1381D1470BB248F6DD606DBB90','B433C67E79B84FE0AE9A6C7B68C9BB3E','Directed','Other','B-'],
    ['D23EA902EA884458ACCF8072D555CDE7','D844F8C3224A4DF38EBEAA9745ADB71B','Directed','Pipe',None],
    ['BA88E57D668647579BF3016108E65EE5','16EFA207185146CC88E262A6752CE04B','Directed','Pipe',None],
    ['596952EFB1D34AA4BFCF64773AF50857','C3320AA78B5D4EAEB49F8E2B98A7A529','Directed','Pipe',None],
    ['792D0312AE8E4A3DA16CA658179D38A2','B8B7989D606A4B5BBFB28F6840986D17','Directed','Pipe',None],
    ['3E303AC1E30542B39391373EFC413239','792D0312AE8E4A3DA16CA658179D38A2','Directed','Pipe',None],
    ['441B037684614EC581B4E02554E4E3CA','51445719BBE2483FA8D2123C5875FA6E','Directed','Pipe',None],
    ['BAF69E705DDF48AA877184E03C4BB52B','3E303AC1E30542B39391373EFC413239','Directed','Pipe',None],
    ['3EF8F05BABDF40259EADC44131819AF0','BAF69E705DDF48AA877184E03C4BB52B','Directed','Pipe',None],
    ['05B5F361E4CD4851AC3F2851660BA5D7','183943A4A00649659B8A81AC8C23EABD','Directed','Pipe',None],
    ['05B5F361E4CD4851AC3F2851660BA5D7','BC9B6CDF14A1452B843D9A1C6D28FB8A','Directed','Pipe',None],
    ['E87EA9C0D1B346F98F4500A422FD4F87','CBC5067AA669438691F35A4D9F316F9A','Directed','Pipe',None],
    ['E2182343C50B4EFCBCF62A52C01469FA','CE35BFB23CFE4A7A906E587AEDF5FE4A','Directed','Pipe',None],
    ['78B19E91F58E41CE8BF250D93F8CABF4','EB3F38B98ED9457BB0A1A697F65D14CD','Directed','Pipe',None],
    ['E9BC66131EB24D9FBEA8881D28B25919','78B19E91F58E41CE8BF250D93F8CABF4','Directed','Pipe',None],
    ['39A7733B0D2047F88CB9A3E649B860A3','E9BC66131EB24D9FBEA8881D28B25919','Directed','Pipe',None],
    ['537AEE5321A649DD8AEE2AA4F56EBA90','BA41295AA3E444B7AF063D4AC1CEABCA','Directed','Pipe',None],
    ['B433C67E79B84FE0AE9A6C7B68C9BB3E','F1E19586B4EB45378E219222F23E81DE','Directed','Pipe',None],
    ['3712D33E3E15451F9E2A0536EFB11BF5','78EA39E83DDB4B419CEA0183172DD619','Directed','Pipe',None],
    ['3712D33E3E15451F9E2A0536EFB11BF5','C6030B1381D1470BB248F6DD606DBB90','Directed','Pipe',None],
    ['78EA39E83DDB4B419CEA0183172DD619','C6030B1381D1470BB248F6DD606DBB90','Directed','Pipe',None],
    ['288EFC7D9B254FD8B38C10660776FF9A','3712D33E3E15451F9E2A0536EFB11BF5','Directed','Pipe',None],
    ['3F0EDC302897422C88BA2269650C237B','3B7B5F5CD4BE4A4D86BF814A9B006219','Directed','Pipe',None],
    ['5F66565B3067499783317018B867B058','288EFC7D9B254FD8B38C10660776FF9A','Directed','Pipe',None],
    ['F0DA3055BB1649A5832776B1042CEEFD','5F66565B3067499783317018B867B058','Directed','Other','XV'],
    ['096E69E3C6D44B4DB767D596AB8A2E09','7105EC5097154D5FBB74C902FE0D5D80','Directed','Pipe',None],
    ['105705F450774C218EA05BBE90970FED','F0DA3055BB1649A5832776B1042CEEFD','Directed','Pipe',None],
    ['308DB54064384D5F8769EAF223D56CE0','3F0EDC302897422C88BA2269650C237B','Directed','Other','HV'],
    ['B90913ACD9EB4181A2719EC49D7BE3DE','105705F450774C218EA05BBE90970FED','Directed','Pipe',None],
    ['B90643B8D5C043A681B0ACF230DF7CBC','2C2BB4952A044DCE96DBD2358BBC1911','Directed','Pipe',None],
    ['B90643B8D5C043A681B0ACF230DF7CBC','7C553E5F56F940089B25CC7F52A285CE','Directed','Other','HV'],
    ['B8B7989D606A4B5BBFB28F6840986D17','596952EFB1D34AA4BFCF64773AF50857','Directed','Other','ES'],
    ['2595E28BB40447F1BDA5716D5CF2CF33','78B19E91F58E41CE8BF250D93F8CABF4','Directed','Pipe',None],
    ['2C2BB4952A044DCE96DBD2358BBC1911','B90643B8D5C043A681B0ACF230DF7CBC','Directed','Pipe',None],
    ['2C2BB4952A044DCE96DBD2358BBC1911','B90913ACD9EB4181A2719EC49D7BE3DE','Directed','Pipe',None],
    ['EB3F38B98ED9457BB0A1A697F65D14CD','3EF8F05BABDF40259EADC44131819AF0','Directed','Pipe',None],
    ['6A1CA6D29CD645058BF2E71637528693','2595E28BB40447F1BDA5716D5CF2CF33','Directed','Pipe',None],
    ['DA75F465071F4B0099024271E55BBB3C','7E235C3F8F704AC5AF5AF139FDC16E0A','Directed','Pipe',None],
    ['DA75F465071F4B0099024271E55BBB3C','83162CF17B244AC28C013F6E18B7CFA1','Directed','Pipe',None],
    ['DA75F465071F4B0099024271E55BBB3C','E46DE2C4256C40DFB236642B2F5EEE4D','Directed','Pipe',None],
    ['FF2A6FBDC9A8418BA7223752DD262C10','B27B64CAA71642DA90B540A0864BF58D','Directed','Other','VA'],
    ['47B23B0B0D2842EE81F10FBD51ACD595','6A1CA6D29CD645058BF2E71637528693','Directed','Other','XV'],
    ['B27B64CAA71642DA90B540A0864BF58D','47B23B0B0D2842EE81F10FBD51ACD595','Directed','Pipe',None],
    ['7C553E5F56F940089B25CC7F52A285CE','B90643B8D5C043A681B0ACF230DF7CBC','Directed','Pipe',None],
    ['7C553E5F56F940089B25CC7F52A285CE','BB9000C0523A446C8D8EBF040001D9AE','Directed','Pipe',None],
    ['C8AC0F7B15BB4296AAB0451CE54CE0C4','A0D1D209BAF4451D97A7638618323CB0','Directed','Other','VA'],
    ['A9A054CF690743A194A1370C128C92BF','ABE0388F75204DA082A420753D0E9B08','Directed','Pipe',None],
    ['A9A8357A4A284F00964452E9BF83B9A2','C3B0074CAE714210BD2D341BBE9708DD','Directed','Pipe',None],
    ['A9A8357A4A284F00964452E9BF83B9A2','E37DCB79E4C64F63B1C071BDAB87A408','Directed','Pipe',None],
    ['876D1314DD694C6E9E913D180DE8FEEB','3F2E00C45FE649EE8A71CA366285E8D5','Directed','Pipe',None],
    ['537D59BD3F004653B62DA5A6F78C5114','084CEBB7191E433FAC9D7E9F442FEAD5','Directed','Other','XV'],
    ['EE01F70565174F28A16E3EE39DEFF941','A9A054CF690743A194A1370C128C92BF','Directed','Pipe',None],
    ['BC9B6CDF14A1452B843D9A1C6D28FB8A','183943A4A00649659B8A81AC8C23EABD','Directed','Pipe',None],
    ['084CEBB7191E433FAC9D7E9F442FEAD5','B944808064D940B0987AA5D873B35CC1','Directed','Pipe',None],
    ['C3320AA78B5D4EAEB49F8E2B98A7A529','BA88E57D668647579BF3016108E65EE5','Directed','Pipe',None],
    ['715C7156BC9B4A4FAC8DE23C1C4BC329','537D59BD3F004653B62DA5A6F78C5114','Directed','Pipe',None]
]

json_data = { 
    'nodes': {}, 
    'edges': []
}

for (i, node) in enumerate(nodes):
    json_data['nodes'][i+1] = {
        'tag': node[0],
        'label': node[1],
        'is_pipe': node[2]
    }
    
for (i, edge) in enumerate(edges):
    dict_edge = {
        'source': edge[0],
        'target': edge[1],
        'type': edge[2],
        'is_pipe': edge[3],
        'other_type': edge[4],
    }
    json_data['edges'].append(dict_edge)
    
    
with open('sample.json', 'w') as outfile:
    outtxt = json.dumps(json_data, indent=4)
    outfile.writelines(outtxt)

def get_label( label ):
    return label
#    json_data['nodes'][label]['tag'][0:8]

def label_node( tag ):
    for label in json_data['nodes'].keys():
        if json_data['nodes'][label]['tag'] == tag:
            return get_label(label)

##
title = "Teste Ladeira."
description = "Grafo gerado saida do programa do Ladeira."

sdf_nodes = "\n"    
for label in json_data['nodes']:
    sdf_nodes += " " * 12 + "<Node label=\"{}\"></Node>\n".format(get_label(label))

sdf_edges = "\n"
for edge in json_data['edges']:
    link_in  = label_node(edge['source'])
    link_out = label_node(edge['target'])
    sdf_edges += " " * 12 + "<Pipe input=\"{}\" output=\"{}\"></Pipe>\n".format(link_in, link_out).ljust(12," ")

with open('sample.sdf', 'w') as outfile:
    outfile.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Project SYSTEM "standard.dtd">
<Project version="1.9  (0)">
    <Network-standard>
        <Title>{}</Title>
        <Network-description>{}</Network-description>
        <Nodes>{}        </Nodes>
        <Links>{}        </Links>
    </Network-standard>
</Project>
""".format(title, description, sdf_nodes, sdf_edges)
)

