class TFDIFMeasure:
     __docs = string[]
	 __ngramDoc = string[][]
	 __numDocs = 0
	 __numTerms = 0
	 ArrayList __terms
	 __termFreq = int[][]
	 __termWeight = float[][]
	 __maxTermFreq = int []
	 __docFreq = int[]
	 
	 
	 ITokeniser _tokenizer = NULL
	 
	 private IDictionary _wordIndex = new Hashtable()
	 def TFIDFMeasure (string[] documents, ITokeniser tokeniser):
	     __docs = documents
		 __numDocs = documents.Length
		 __tokenizer = tokeniser
		 MyInit()
	
	 def NumTerms():
         get{ return __numTerms}
         set{ __numTerms = value}
		
     def ArrayList GenerateTerms (string[] docs):
	     ArrayList uniques = new ArrayList()
		 __ngramDoc = new string[__numDocs][]
		 for i in range(doc.Length):
		     IList<string> words = __tokenizer.Partition(docs[i])
			 for j in range(words.Count):
			     if (!uniques.Contains(words[j])):
				     uniques.Add(words[j])
		 return uniques
		 
	 def object AddElemenet(IDictionary collection, object key, object newValue):
	     object element = collection[key]
         collection[key] = newValue		
         return element		 
	 
	 def MyInit():
	     __terms = GenerateTerms(__docs)
		 NumTerms = __terms.Count
		 
		 __maxTermFreq = =new int[__numDocs]
		 __docFreq = new int[NumTerms]
		 __termFreq = new int[NumTerms][]
		 __termWeight = new float[NumTerms][]
		 
		 for i in range(__terms.Count):
		     __termWeight[i] = new float[__numDocs]
			 __termFreq[i] = new int[__numDocs]
			 
			 AddElement(__wordsIndex, __terms[i],i)
		 
		 GenerateTermFrequency()
		 GenerateTermWight()
	
     def GenerateTermFrequency():
         for i in range(__numDocs):
             string curDoc = __docs[i]	
             IDictionary freq = GetWordFrequency (curDoc)
             IDictionaryEnumerator enums = freq.GetEnumerator()
             __maxTermFreq[i] = int.MinValue
             while(enums.MoveNext()):
                 string word = (string)enums.KeyError
                 int wordFreq = (int)enums.Value
				 int termIndex = GetTermIndex(word)
				 if (termIndex == -1):
				     continue
				 __termFreq[termIndex][i] = wordFreq
				 __docFreq[termIndex]++
				 
				 if (wordFreq > __maxTermFreq[i]):
				     _maxTermFreq[i] = wordFreq
                  				 




     def IDictionary GetWordFrequency(string input):
	     string convertedInput = input.ToLower()
		 List<string> temp = new List<string>(__tokenizer.Partition(convertedInput))
		 string[] words = temp.ToArray()
		 
		 Array.Sort(words)
		 String[] distinctWords = GetDistinctWords(words)
		 
		 IDictionary result = new Hashtable()
		 for i in range(distinctWords.Length):
		     object tmp
			 tmp = CountWords(distinctWords[i], words)
			 result[distinctWords[i]] = tmp
		 return result
          	 




     def static string[] GetDistinctWords(String[] input):
	     if input == null:
		     return new string[0]
		 else :
		     List<string> list = new List<string>()
			 for i in range(input.Length):
			     if (!list.Contains(input[i])):
				     list.Add(input[i])
			 return list.ToArray()
             		 
     def CountWords(string word, string[] words):
	     int itemIdx = Array.BinarySearch(words, word)//二分法查找
		 if (itemIdx > 0):
		     while(itemIdx > 0 && words[itemIdx].Equals(word)):
			 itemIdx--
			 
		 int count = 0
		 while(itemIdx < words.Length && itemIdx >=0):
		     if words[itemIdx].Equals(word):
			     count ++; itemIdx++
			 if itemIdx < words.Length:
			     if !words[itemIdx].Equals(word):
				     break
		 return count
		 
     def GenerateTermWight():
	     for i in range(NumTerms):
		     for j in range(__numDocs):
			     __termWeight[i][j] = ComputeTermWeight(i,j)















			 
