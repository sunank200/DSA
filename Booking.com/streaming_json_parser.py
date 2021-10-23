"""
Deprecated Coding Interview question:

Please use this question below to practice and also get an idea of what you can
expect during the actual interview. This question can be solved in a lot of
different ways, some quick and naive, others more advanced that encompass a
lot of edge cases. What we are looking for during the interview is that you
lead a discussion around the subject matter and are able to tackle the problem
not only from the technical perspective but also from the business and user
perspective. Also expect more challenging follow up questions than the ones
listed below.


Streaming JSON Parser
---------------------------------
You are given an open socket handler. The api for this handler looks like:

$socket_handler->get_next_char(), which returns a single character at a time
and moves the handler pointer forward, and:

$socker_handler->is_eof(), which returns a boolean indicating if it’s reached
the end of the stream.

We know nothing about the data size: it’s unbounded. The only thing that’s
known about it: it’s a sequence of valid JSON documents.

Your goal is to implement a streaming JSON parser, which should search for a
specific key in the stream.


Example:


sub search {

    my ($socket_handler, $search_path) = @_;

# TODO: implement me

}


my $socket_handler = open_handler(...)

or die ‘Unable to open handler: ’ . $@;


search($socket_handler, ‘lookup_key’) // should output everything as a string
to STDOUT if it found this key in the document.


An example of the data that might be read from the socket:


{“k1”: 1, “k2”: {“k3”: [“a”, “b”, “c”]}, “lookup_key”: {“a”: 1, “b”: [2]}}

Expected output: {“a”: 1, “b”: [2]}.


Remember: the data size might be way bigger than the RAM available for
your application, so reading the data entirely is not an option.



Follow-up questions to prepare for:

Extend the solution to support JSON path: support more complex lookup logic,
 e.g.: lookup_key.a, or: lookup_key.b[0]
Can you reason about parallelisation possibilities?

"""
