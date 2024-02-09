def euclidean_distance(vector1, vector2):
    # the length of the two vectors shold be same for distance caluclation
    if len(vector1) != len(vector2):
        return 'dimension odf the vector is not same'
    squared_distance = 0
    # caluclating the euclidean distance for for the two vectors
    for i in range(len(vector1)):
        squared_distance = squared_distance+(vector1[i]-vector2[i]) ** 2
    return squared_distance ** 0.5


def manhattan_distance(vector1, vector2):
    # the length of the two vectors shold be same for distance caluclation
    if len(vector1) != len(vector2):
        return 'dimension odf the vector is not same'
    distance = 0
    # caluclating the manhattan distance for for the two vectors
    for i in range(len(vector1)):
        distance = distance+abs(vector1[i]-vector2[i])
    return distance


vector1 = [1, 2]
vector2 = [2, 4]
print("euclidean distance=", euclidean_distance(vector1, vector2))
print("manhattan distance=", manhattan_distance(vector1, vector2))


def K_Nearest_Neighbors(k, data_points):
    distances = []
    for i in range(1, len(data_points)):
        calculated_Distance = euclidean_distance(
            data_points[0], data_points[i])
        distances.append((calculated_Distance, data_points[i][2]))

    for j in range(len(distances)):
        for l in range(0, len(distances) - j - 1):
            if distances[l][0] > distances[l+1][0]:
                distances[l], distances[l+1] = distances[l+1], distances[l]

    k_nearest = distances[:k]

    frequency_class1 = 0
    for distance, label in k_nearest:
        if label == 1:
            frequency_class1 += 1

    frequency_class2 = k - frequency_class1

    if frequency_class1 > frequency_class2:
        return "belongs to the First Class"
    else:
        return "belongs to the Second Class"


def encode_labels(labels):
    Unique_label_set = set(labels)
    Label_to_code = {}
    code = 0

    for label in Unique_label_set:
        Label_to_code[label] = code
        code += 1

    for label in labels:
        encoded_label = Label_to_code[label]

    return encoded_label, Label_to_code


def one_hot_encode(labels):
    Unique_labels = sorted(set(labels))
    one_hot_encoding = {}

    for label in Unique_labels:
        one_hot_encoding[label] = [0] * len(Unique_labels)

    for i, label in enumerate(Unique_labels):
        one_hot_encoding[label][i] = 1
    encoded_labels = []
    for label in labels:
        one_hot_encoding[label]

    return encoded_labels, one_hot_encoding


def read_arff_file(file_path):
    with open(file_path, 'r') as f:
        text = f.readline()

    attributes = []
    data = []
    labels = []
    read_data = False

    for line in text:
        line = text.strip()

        if not line or text.startswith('%'):
            continue

        if line.lower().startswith('@attribute'):
            attribute_name = line.split()[1]
            attributes.append(attribute_name)

        elif line.lower().startswith('@data'):
            read_data = True

        elif read_data:
            data.append(line.split(','))

        elif line.lower().startswith('@relation'):
            relation_name = line.split()[1]

        elif line.lower().startswith('{'):
            labels.extend(line.strip('{}').split(','))

    return data, attributes, labels


file_path = "medical.arff"
Data, Attributes, Labels = read_arff_file(file_path)

coordinates = []
for row in Data:
    for value in row[:-1]:
        featured_value = float(value)
        tuple(featured_value)
        label = int(row[-1])

        coordinates.append((featured_value, label))


k = int(input("Enter a certain value of k = "))
read_arff_file("medical.arff")
result = K_Nearest_Neighbors(k, coordinates)
print("Classification result:", result)
