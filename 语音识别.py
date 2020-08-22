#将录音录入后，对比以前的乐器四特征（声道数一般固定为1  量化位数 采样频率 采样点数 ）
import wave
import json
def Read_WAV(wav_path):
    """
    这是读取wav文件的函数
    :param wav_path: WAV文件的地址
    """
    wav_file = wave.open(wav_path,'r')
    numchannel = wav_file.getnchannels()          # 声道数
    samplewidth = wav_file.getsampwidth()      # 量化位数
    framerate = wav_file.getframerate()        # 采样频率
    numframes = wav_file.getnframes()           # 采样点数
    print("channel", numchannel)
    print("sample_width", samplewidth)
    print("framerate", framerate)
    print("numframes", numframes)
    Wav_Data = wav_file.readframes(numframes)
    Wav_Data = np.fromstring(Wav_Data,dtype=np.int16)
    Wav_Data = Wav_Data*1.0/(max(abs(Wav_Data)))        #对数据进行归一化
    # 生成音频数据,ndarray不能进行json化，必须转化为list，生成JSON
    dict = {"channel":numchannel,
            "samplewidth":samplewidth,
            "framerate":framerate,
            "numframes":numframes,
            "WaveData":list(Wav_Data)}
    return json.dumps(dict)
# 开始对音频文件进行数据化
def result():
    for wav_path in wav_paths:
        wav_json = Read_WAV(wav_path)
        print(wav_json)
        wav = json.loads(wav_json)
        wav_data = np.array(wav['WaveData'])#(音频数据)
        framerate = int(wav['framerate'])#（采样频率）
def change():
    #通过对比特征来进行转换

