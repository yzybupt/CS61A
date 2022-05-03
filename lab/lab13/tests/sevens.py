test = {
  'name': 'sevens',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          seven
          7
          7
          7
          7
          7
          Choose this option instead
          7
          7
          7
          7
          seven
          7
          7
          Choose this option instead
          7
          7
          7
          7
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
